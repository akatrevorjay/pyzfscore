#!/usr/bin/env python

#from .. import _cffi
#from .._cffi import czfs, czpool, cnvpair, ptop, cdef, ffi, boolean_t
#from .._cffi import boolean_t
from . import _cffi, consts
from ._cffi import ffi, boolean_t


from .consts import libzfs_errors, \
        zprop_source_t, \
        zfs_prop_t, zfs_type_t, zfs_userquota_prop_t, \
        zpool_prop_t, zpool_status_t, \
        pool_state_t

from .czfs import czfs


""" Library initialization """


def libzfs_fini(zhp):
    """Closes libzfs_handle"""
    return czfs.libzfs_fini(zhp)


def libzfs_init():
    """Initialize libzfs_handle"""
    return ffi.gc(czfs.libzfs_init(), libzfs_fini)


def zpool_get_handle(zhp):
    """Get libzfs handle from zpool_handle"""
    return czfs.zpool_get_handle(zhp)


def zfs_get_handle(zhp):
    """Get libzfs handle from zfs_handle"""
    return czfs.zpool_get_handle(zhp)


def libzfs_print_on_error(zhp, value=True):
    value = ffi.cast('boolean_t', value)
    return czfs.libzfs_print_on_error(zhp, value)


def libzfs_errno(zhp):
    return czfs.libzfs_errno(zhp)


def libzfs_error_action(zhp):
    return ffi.string(czfs.libzfs_error_action(zhp))


def libzfs_error_description(zhp):
    return ffi.string(czfs.libzfs_error_description(zhp))


""" Basic handle functions """


def zpool_close(zhp):
    """Close zpool_handle"""
    return czfs.zpool_close(zhp)


def zpool_open(zhp, name):
    """Open zpool_handle"""
    return ffi.gc(czfs.zpool_open(zhp, name), zpool_close)


def zpool_get_name(zhp):
    """Get name for zpool_handle"""
    return ffi.string(czfs.zpool_get_name(zhp))


def zpool_get_state(zhp):
    """Returns state for zpool_handle"""
    state = czfs.zpool_get_state(zhp)
    return pool_state_t[state]


def zpool_state_to_name(vdev_state, vdev_aux):
    """Map VDEV STATE to printed strings."""
    return ffi.string(czfs.zpool_state_to_name(vdev_state, vdev_aux))


def zpool_pool_state_to_name(pool_state):
    """Map POOL STATE to printed strings."""
    return ffi.string(czfs.zpool_pool_state_to_name(pool_state))


def zpool_free_handles(zhp):
    return czfs.zpool_free_handles(zhp)


""" Iterate over all active pools in the system """


def zpool_iter(zhp, handler, arg=None):
    return czfs.zpool_iter(zhp, handler, ffi.new_handle(arg))


""" Functions to manipulate pool and vdev state """


#def zpool_clear(zhp, blah, nvblah):
#    pass


""" Pool health statistics """


def zpool_get_status(zhp, arg=None):
    """Get status of zpool"""
    return czfs.zpool_get_status(zhp, arg)


"""
Basic handle manipulations.  These functions do not create or destroy the
underlying datasets, only the references to them.
"""


def zfs_close(zhp):
    """Closes zfs_handle"""
    return czfs.zfs_close(zhp)


def zfs_open(zhp, name, types_mask=sum(zfs_type_t)):
    """Gets zfs_handle for dataset"""
    return ffi.gc(czfs.zfs_open(zhp, name, types_mask), zfs_close)


def zfs_handle_dup(zhp):
    """Duplicates zfs_handle"""
    return ffi.gc(czfs.zfs_handle_dup(zhp), zfs_close)


def zfs_get_type(zhp):
    """Gets type for zfs_handle"""
    return zfs_type_t[czfs.zfs_get_type(zhp)]


def zfs_get_name(zhp):
    """Gets name for zfs_handle"""
    return ffi.string(czfs.zfs_get_name(zhp))


def zfs_get_pool_handle(zhp):
    """Gets pool handle for zfs_handle"""
    return czfs.zfs_get_pool_handle(zhp)


""" Iterator functions """


def zfs_iter_root(zhp, handler, arg=None):
    return czfs.zfs_iter_root(zhp, handler, ffi.new_handle(arg))

def zfs_iter_children(zhp, handler, arg=None):
    return czfs.zfs_iter_children(zhp, handler, ffi.new_handle(arg))

# TODO what is boolean_t for? Name accordingly.
def zfs_iter_dependents(zhp, b, handler, arg=None):
    return czfs.zfs_iter_dependents(zhp, b, handler, ffi.new_handle(arg))

def zfs_iter_filesystems(zhp, handler, arg=None):
    return czfs.zfs_iter_filesystems(zhp, handler, ffi.new_handle(arg))

# TODO what is boolean_t for? Name accordingly.
def zfs_iter_snapshots(zhp, b, handler, arg=None):
    return czfs.zfs_iter_snapshots(zhp, b, handler, ffi.new_handle(arg))

def zfs_iter_snapshots_sorted(zhp, handler, arg=None):
    return czfs.zfs_iter_snapshots_sorted(zhp, handler, ffi.new_handle(arg))

# TODO what is const char * for? Name accordingly.
def zfs_iter_snapspec(zhp, c, handler, arg=None):
    return czfs.zfs_iter_snapspec(zhp, c, handler, ffi.new_handle(arg))


""" Functions to create and destroy datasets. """


def zfs_destroy(zhp, defer=True):
    return czfs.zfs_destroy(zhp, boolean_t(defer))


""" Miscellaneous functions. """


def zfs_type_to_name(zfs_type_t):
    return ffi.string(czfs.zfs_type_to_name(zfs_type_t))


def zfs_refresh_properties(zhp):
    return czfs.zfs_refresh_properties(zhp)


def zfs_name_valid(name, zfs_type_t=zfs_type_t.ALL):
    return czfs.zfs_name_valid(name, zfs_type_t)


def zfs_dataset_exists(zhp, name, zfs_type_t=zfs_type_t.ALL):
    return bool(czfs.zfs_dataset_exists(zhp, name, zfs_type_t))


""" Mount support functions. """


def zfs_is_mounted(zhp):
    """If @zfs_handle:zhp is mounted, return path where"""
    where = ffi.new('char **')
    ret = czfs.zfs_is_mounted(zhp, where)
    if ret:
        return ffi.string(where[0])
