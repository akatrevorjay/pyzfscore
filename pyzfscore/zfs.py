#!/usr/bin/env python


from ._cffi import ffi
from . import libzfs
from .libzfs import zfs_type_t


LZH = libzfs.libzfs_init()


class _ZBase(object):
    _zfs_type_mask = zfs_type_t.ALL

    _lzh = LZH
    name = None

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)


class ZDataset(_ZBase):
    _zfs_type_mask = zfs_type_t.DATASET

    @classmethod
    def _exists(cls, name, type_mask=None):
        if not type_mask:
            type_mask = cls._zfs_type_mask
        return libzfs.zfs_dataset_exists(cls._lzh, name, type_mask)

    @classmethod
    def open(cls, name):
        if not cls._exists(name):
            return
        handle = libzfs.zfs_open(cls._lzh, name, cls._zfs_type_mask)
        return cls.from_handle(handle)

    @classmethod
    def _find_subclass_for_type_mask(cls, type_mask):
        for scls in cls.__subclasses__():
            if type_mask & scls._zfs_type_mask:
                return scls
        return cls

    @classmethod
    def from_handle(cls, handle):
        # Find type on init of ZDataset from_handle and use proper subclass
        handle_type = libzfs.zfs_get_type(handle)
        # TODO is there a way to trawl up mro to find the parent without
        # specifying the hard class name here?
        handle_cls = ZDataset._find_subclass_for_type_mask(handle_type)

        self = handle_cls()
        self._handle = handle
        self._load()
        return self

    @classmethod
    def iter_root(cls):
        return cls._children_iterator(libzfs.zfs_iter_root, [cls._lzh])

    list = iter_root

    def _get_libzfs_handle(self):
        return libzfs.zfs_get_handle(self._handle)

    def _load(self):
        self.name = libzfs.zfs_get_name(self._handle)

    """ Path helpers """

    def path(self, start=0, len=None):
        """ Splits name of object into paths starting at index start """
        return self.name.split('/')[start:len]

    @property
    def basename(self):
        return self.path(-1)[0]

    """ Parent traversal """

    @property
    def pool_name(self):
        name = self.path(0, 1)[0]
        if '@' in name:
            name = name.split('@', 1)[0]
        return name

    def to_pool(self):
        #return ZPool.open(self.pool_name)
        handle = libzfs.zfs_get_pool_handle(self._handle)
        return ZPool.from_handle(handle)

    @property
    def parent_name(self):
        """ Returns the associated filesystem/volume name """
        pname = self.path(0, -1)
        # We may not have a parent
        if pname:
            return '/'.join(pname)

    def to_parent(self):
        return ZDataset.open(self.parent_name)

    """ Dataset tests """

    def is_mounted(self):
        return libzfs.zfs_is_mounted(self._handle)

    """ Child traversal """

    def open_child(self, name):
        sep = ''
        if not name.startswith('@') or name.startswith('/'):
            sep = '/'
        full_name = '%s%s%s' % (self.name, sep, name)
        return ZDataset.open(full_name)

    def open_child_snapshot(self, name):
        full_name = '%s@%s' % (self.name, name)
        return ZSnapshot.open(full_name)

    def open_child_filesystem(self, name):
        full_name = '%s/%s' % (self.name, name)
        return ZFilesystem.open(full_name)

    def open_child_volume(self, name):
        full_name = '%s/%s' % (self.name, name)
        return ZVolume.open(full_name)

    """ Child iteration """

    @classmethod
    def _children_iterator(cls, func, args):
        children = []

        @libzfs.ffi.callback('zfs_iter_f')
        def _zfs_iter_cb(handle, arg=None):
            c = cls.from_handle(handle)
            children.append(c)
            return 0

        args.append(_zfs_iter_cb)
        # TODO instead of args would partials be better?
        func(*args)
        return children

    def iter_children(self):
        return self._children_iterator(libzfs.zfs_iter_children, [self._handle])

    def iter_filesystems(self):
        return self._children_iterator(libzfs.zfs_iter_filesystems, [self._handle])

    def iter_snapshots_sorted(self):
        return self._children_iterator(libzfs.zfs_iter_snapshots_sorted, [self._handle])

    """ Dataset operations """

    def destroy(self, defer=True):
        return libzfs.zfs_destroy(self._handle, defer)

    """ Property operations """

    def prop_get(self, name, literal=False):
        return libzfs.zfs_prop_get(self._handle, name, literal=literal)

    def prop_set(self, name, value):
        return libzfs.zfs_prop_set(self._handle, name, value)


class _SnapshottableZDataset:
    # TODO props
    def snapshot(self, name, recursive=False):
        full_name = '%s@%s' % (self.name, name)
        return libzfs.zfs_snapshot(self._lzh, full_name, recursive=recursive)

    def destroy_snapshot(self, name, defer=True, recursive=False):
        full_name = '%s@%s' % (self.name, name)
        snapshot = ZSnapshot.open(full_name)
        return snapshot.destroy(defer=defer, recursive=recursive)


class ZFilesystem(ZDataset, _SnapshottableZDataset):
    _zfs_type_mask = zfs_type_t.ZFS_TYPE_FILESYSTEM


class ZVolume(ZDataset, _SnapshottableZDataset):
    _zfs_type_mask = zfs_type_t.ZFS_TYPE_VOLUME


class ZSnapshot(ZDataset):
    _zfs_type_mask = zfs_type_t.ZFS_TYPE_SNAPSHOT

    """ Path helpers """

    @property
    def parent_name(self):
        """ Returns the associated filesystem/volume name """
        return self.name.rsplit('@', 1)[0]

    filesystem_name = parent_name

    @property
    def snapshot_name(self):
        """ Returns the snapshot name """
        return self.basename.rsplit('@', 1)[1]

    @property
    def filesystem_basename(self):
        """ Returns the associated filesystem/volume name """
        return self.basename.rsplit('@', 1)[0]

    def destroy(self, defer=True, recursive=False):
        if not recursive:
            return super(ZSnapshot, self).destroy(defer=defer)
        else:
            parent = self.to_parent()
            return libzfs.zfs_destroy_snaps(parent._handle,
                                            self.snapshot_name,
                                            defer)


class ZPool(_ZBase):
    _zfs_type_mask = zfs_type_t.ZFS_TYPE_POOL

    @classmethod
    def iter(cls):
        pools = []

        @libzfs.ffi.callback('zpool_iter_f')
        def _zpool_iter_cb(handle, arg=None):
            p = cls.from_handle(handle)
            pools.append(p)
            return 0

        libzfs.zpool_iter(cls._lzh, _zpool_iter_cb)
        return pools

    list = iter

    @classmethod
    def from_handle(cls, handle):
        self = cls()
        self._handle = handle
        self._load()
        return self

    @classmethod
    def open(cls, name):
        handle = libzfs.zpool_open(cls._lzh, name)
        #handle = libzfs.zpool_open_canfail(cls._lzh, name)
        return cls.from_handle(handle)

    def _get_libzfs_handle(self):
        return libzfs.zpool_get_handle(self._handle)

    def _load(self):
        self.name = libzfs.zpool_get_name(self._handle)
        self.active = self._is_active()
        if self.active:
            self.filesystem = self._to_filesystem()
            self.state = self._get_state()

    def _is_active(self):
        return self._get_state() == 'ACTIVE'

    def _to_filesystem(self):
        return ZFilesystem.open(self.name)

    def _get_state(self):
        pool_state = libzfs.zpool_get_state(self._handle)
        return libzfs.zpool_pool_state_to_name(pool_state)
