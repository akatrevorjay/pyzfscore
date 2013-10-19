#!/usr/bin/env python


from ._cffi import ffi
from . import libzfs


LZH = libzfs.libzfs_init()


class _ZBase(object):
    _types_mask = sum(libzfs.zfs_type_t)

    _lzh = LZH
    name = None

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)


class ZDataset(_ZBase):
    _types_mask = libzfs.zfs_type_t.ZFS_TYPE_FILESYSTEM | libzfs.zfs_type_t.ZFS_TYPE_SNAPSHOT | libzfs.zfs_type_t.ZFS_TYPE_VOLUME

    @classmethod
    def open(cls, name):
        handle = libzfs.zfs_open(cls._lzh, name, cls._types_mask)
        return cls.from_handle(handle)

    @classmethod
    def _find_subclass_for_type_mask(cls, type_mask):
        for scls in cls.__subclasses__():
            if type_mask & scls._types_mask:
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
        #self._lzh = libzfs.zfs_get_handle(handle)
        self._handle = handle
        self._load()
        return self

    def _load(self):
        self.name = libzfs.zfs_get_name(self._handle)

    @classmethod
    def _children_iterator(cls, func, args):
        children = []

        @ffi.callback('zfs_iter_f')
        def _zfs_iter_cb(handle, arg=None):
            c = cls.from_handle(handle)
            children.append(c)
            return 0

        args.append(_zfs_iter_cb)
        # TODO instead of args would partials be better?
        func(*args)
        return children

    @classmethod
    def iter_root(cls):
        return cls._children_iterator(libzfs.zfs_iter_root, [cls._lzh])

    list = iter_root

    def iter_children(self):
        return self._children_iterator(libzfs.zfs_iter_children, [self._handle])

    def iter_filesystems(self):
        return self._children_iterator(libzfs.zfs_iter_filesystems, [self._handle])

    def iter_snapshots_sorted(self):
        return self._children_iterator(libzfs.zfs_iter_snapshots_sorted, [self._handle])

    def to_pool(self):
        handle = libzfs.zfs_get_pool_handle(self._handle)
        return ZPool.from_handle(handle)

    def destroy(self, defer=True):
        return libzfs.zfs_destroy(self._handle, defer)


class ZFilesystem(ZDataset):
    _types_mask = libzfs.zfs_type_t.ZFS_TYPE_FILESYSTEM


class ZSnapshot(ZDataset):
    _types_mask = libzfs.zfs_type_t.ZFS_TYPE_SNAPSHOT


class ZVolume(ZDataset):
    _types_mask = libzfs.zfs_type_t.ZFS_TYPE_VOLUME


class ZPool(_ZBase):
    _types_mask = libzfs.zfs_type_t.ZFS_TYPE_POOL

    @classmethod
    def iter(cls):
        pools = []

        @ffi.callback('zpool_iter_f')
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
        #self._lzh = libzfs.zpool_get_handle(handle)
        self._handle = handle
        self._load()
        return self

    @classmethod
    def open(cls, name):
        handle = libzfs.zpool_open(cls._lzh, name)
        return cls.from_handle(handle)

    def _load(self):
        self.name = libzfs.zpool_get_name(self._handle)
        # TODO Check if dataset/pool exists and is active before doing this
        # otherwise it segfaults
        #self.filesystem = self.to_filesystem()

    def to_filesystem(self):
        return ZFilesystem.open(self.name)
