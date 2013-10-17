#!/usr/bin/env python


from _cffi import ffi
import libzfs

LZH = libzfs.libzfs_init()


class _ZBase(object):
    _types_mask = 1 + 2 + 4 + 8

    _lzh = LZH
    name = None

    #def __init__(self, _lzh=None):
    #    self._lzh = _lzh
    #    if not self._lzh:
    #        self._lzh = libzfs.libzfs_init()

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)


class ZDataset(_ZBase):
    _types_mask = 1 + 2 + 4

    @classmethod
    def open(cls, name):
        handle = libzfs.zfs_open(cls._lzh, name, cls._types_mask)
        return cls.from_handle(handle)

    @classmethod
    def from_handle(cls, handle):
        self = cls()
        self._handle = handle
        self._load()
        return self

    def _load(self):
        self.name = libzfs.zfs_get_name(self._handle)


class ZFilesystem(ZDataset):
    _types_mask = 1


class ZSnapshot(ZDataset):
    _types_mask = 2


class ZVolume(ZDataset):
    _types_mask = 4


class ZPool(_ZBase):
    _types_mask = 8

    def __init__(self):
        pass

    @classmethod
    def list(cls):
        pools = []

        @ffi.callback('zpool_iter_f')
        def _zpool_iter_cb(handle, arg=None):
            p = cls.from_handle(handle)
            pools.append(p)
            return 0

        libzfs.zpool_iter(cls._lzh, _zpool_iter_cb)
        return pools

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
        self.filesystem = ZFilesystem.open(self.name)
