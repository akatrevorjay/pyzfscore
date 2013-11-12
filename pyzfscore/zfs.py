#!/usr/bin/env python


from ._cffi import ffi
from . import libzfs
from .libzfs import zfs_type_t
from . import libnvpair


LZH = libzfs.libzfs_init()


class _ZBase(object):
    _zfs_type_mask = zfs_type_t.ALL

    _lzh = LZH
    name = None

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)


class _ZBaseProperty(object):

    """ Base Property object. """

    def __init__(self, parent, name, value, source):
        self._parent = parent
        self._dataset = parent._parent
        self.name = name
        self._set(value, ignore=True)
        self.source = source

    def __repr__(self):
        return "%s('%s'='%s' src='%s')" % (self.__class__.__name__, self.name, self.value, self.source)

    def __unicode__(self):
        return unicode(self.value)

    def __str__(self):
        return str(self.value)

    def __bool__(self):
        value = self.value
        if value == 'on':
            return True
        elif value == 'off':
            return False
        else:
            return bool(value)

    #def __nonzero__(self):
    #    value = self.value
    #    if value == 'on':
    #        return True
    #    elif value:
    #        return False

    @property
    def is_local(self):
        return self.source == self._dataset.name

    def _get(self):
        return self._value

    def _set(self, value, ignore=False):
        if not ignore:
            self._parent._set(self.name, value)
        self._value = value

    value = property(_get, _set)


class _ZBaseProperties(object):

    """ Base Properties object. """

    def __init__(self, parent):
        self._parent = parent

    """ Magic """

    def __getitem__(self, k):
        """Get dataset property.

        dataset = Dataset('dpool/carp')
        dataset.properties['alloc']

        """
        # TODO return KeyError if not found
        return self._get(k)

    def __setitem__(self, k, v):
        """Set dataset property.

        dataset = Dataset('dpool/carp')
        dataset.properties['readonly'] = 'on'

        """
        # TODO return ValueError if not found
        return self._set(k, v)

    def __delitem__(self, k):
        """ Delete dataset property. """
        # TODO raise KeyError on non existent
        return self._inherit(k)


class ZDatasetProperty(_ZBaseProperty):

    """ Dataset Property object. """


class ZDatasetProperties(_ZBaseProperties):

    """ Storage Dataset Properties object. """

    def _get(self, name, literal=False):
        """Get dataset property."""
        if not libzfs.zfs_prop_user(name):
            value = libzfs.zfs_prop_get(self._parent._handle, name, literal=literal)
            # TODO source
            source = None
        else:
            # TODO how to get a single userprop?
            nvl = libzfs.zfs_get_user_props(self._parent._handle)
            nvl = libnvpair.NVList.from_nvlist_p(nvl)
            nvl_prop = nvl.lookup_nvlist(name)
            if nvl_prop:
                value = nvl_prop.lookup_string('value')
                source = nvl_prop.lookup_string('source')
        return ZDatasetProperty(self, name, value, source)

    def _set(self, name, value):
        """Set Dataset property."""
        ret = libzfs.zfs_prop_set(self._parent._handle, name, value)
        return ret

    # TODO Delete item == inherit property
    def _inherit(self, k):
        """Inherit property from parents."""
        raise NotImplementedError


class ZDataset(_ZBase):
    _zfs_type_mask = zfs_type_t.DATASET

    def __init__(self):
        self.props = ZDatasetProperties(self)

    @classmethod
    def _exists(cls, name, type_mask=None):
        """Class method that returns if dataset exists.
        """
        if not type_mask:
            type_mask = cls._zfs_type_mask
        return libzfs.zfs_dataset_exists(cls._lzh, name, type_mask)

    def exists(self):
        """Returns if dataset exists.
        """
        return self._exists(self.name)

    @classmethod
    def open(cls, name):
        """Opens a dataset object by name.
        """
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
        """Creates a dataset object from an existing zfs_handle.
        """
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
        """Iterates through root datasets.
        """
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
        """ Returns the parent filesystem/volume name """
        pname = self.path(0, -1)
        # We may not have a parent
        if pname:
            return '/'.join(pname)

    @property
    def parent_basename(self):
        """ Returns the parent filesystem/volume basename """
        pname = self.path(0, -1)
        # We may not have a parent
        if pname:
            return pname[-1]

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
    def filesystem_name(self):
        """ Returns the associated filesystem/volume name """
        return self.name.rsplit('@', 1)[0]

    parent_name = filesystem_name

    @property
    def filesystem_basename(self):
        """ Returns the associated filesystem/volume name """
        return self.basename.rsplit('@', 1)[0]

    parent_basename = filesystem_basename

    @property
    def snapshot_name(self):
        """ Returns the snapshot name """
        return self.basename.rsplit('@', 1)[1]

    def destroy(self, defer=True, recursive=False):
        if not recursive:
            return super(ZSnapshot, self).destroy(defer=defer)
        else:
            parent = self.to_parent()
            return libzfs.zfs_destroy_snaps(parent._handle,
                                            self.snapshot_name,
                                            defer)

    def hold(self, tag):
        # TODO Hold snapshot
        raise NotImplementedError

    def release(self, tag):
        # TODO Release snapshot
        raise NotImplementedError


class ZPoolProperty(_ZBaseProperty):

    """ Pool Property object. """


class ZPoolProperties(_ZBaseProperties):

    """ Storage Pool Properties object. """

    def _get(self, name, literal=False):
        """Get dataset property."""
        raise NotImplementedError

    def _set(self, name, value):
        """Set Pool property."""
        raise NotImplementedError

    # TODO Delete item == inherit property
    def _inherit(self, k):
        """Inherit property from parents."""
        raise NotImplementedError


class ZPool(_ZBase):
    _zfs_type_mask = zfs_type_t.ZFS_TYPE_POOL

    def __init__(self):
        self.props = ZPoolProperties(self)

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
