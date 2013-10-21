#!/usr/bin/env python

#from .. import _cffi
#from .._cffi import czfs, czpool, cnvpair, ptop, cdef, ffi, boolean_t
#from .._cffi import boolean_t
from . import _cffi, consts
from ._cffi import ffi


from .consts import libzfs_errors, \
        zprop_source_t, \
        zfs_prop_t, zfs_type_t, zfs_userquota_prop_t, \
        zpool_prop_t, zpool_status_t, \
        pool_state_t

from .czfs import czfs


""" Library initialization """


#ffi.cdef('void libzfs_fini(libzfs_handle_t *);')
def libzfs_fini(zhp):
    """Closes libzfs_handle"""
    return czfs.libzfs_fini(zhp)


#ffi.cdef('libzfs_handle_t *libzfs_init(void);')
def libzfs_init():
    """Initialize libzfs_handle"""
    return ffi.gc(czfs.libzfs_init(), libzfs_fini)


#ffi.cdef('libzfs_handle_t *zpool_get_handle(zpool_handle_t *);')
def zpool_get_handle(zhp):
    """Get libzfs handle from zpool_handle"""
    return czfs.zpool_get_handle(zhp)


#ffi.cdef('libzfs_handle_t *zfs_get_handle(zfs_handle_t *);')
def zfs_get_handle(zhp):
    """Get libzfs handle from zfs_handle"""
    return czfs.zpool_get_handle(zhp)


#ffi.cdef('void libzfs_print_on_error(libzfs_handle_t *, boolean_t);')
def libzfs_print_on_error(zhp, value=True):
    value = ffi.cast('boolean_t', value)
    return czfs.libzfs_print_on_error(zhp, value)


#ffi.cdef('int libzfs_errno(libzfs_handle_t *);')
def libzfs_errno(zhp):
    return czfs.libzfs_errno(zhp)


#ffi.cdef('const char *libzfs_error_action(libzfs_handle_t *);')
def libzfs_error_action(zhp):
    return ffi.string(czfs.libzfs_error_action(zhp))


#ffi.cdef('const char *libzfs_error_description(libzfs_handle_t *);')
def libzfs_error_description(zhp):
    return ffi.string(czfs.libzfs_error_description(zhp))


""" Basic handle functions """


#ffi.cdef('void zpool_close(zpool_handle_t *);')
def zpool_close(zhp):
    """Close zpool_handle"""
    return czfs.zpool_close(zhp)


#ffi.cdef('zpool_handle_t *zpool_open(libzfs_handle_t *, const char *);')
def zpool_open(zhp, name):
    """Open zpool_handle"""
    return ffi.gc(czfs.zpool_open(zhp, name), zpool_close)


#ffi.cdef('const char *zpool_get_name(zpool_handle_t *);')
def zpool_get_name(zhp):
    """Get name for zpool_handle"""
    return ffi.string(czfs.zpool_get_name(zhp))


#ffi.cdef('int zpool_get_state(zpool_handle_t *);')
def zpool_get_state(zhp):
    """Returns state for zpool_handle"""
    state = czfs.zpool_get_state(zhp)
    return pool_state_t[state]


#ffi.cdef('char *zpool_state_to_name(vdev_state_t, vdev_aux_t);')
def zpool_state_to_name(vdev_state, vdev_aux):
    """Map VDEV STATE to printed strings."""
    return ffi.string(czfs.zpool_state_to_name(vdev_state, vdev_aux))


#ffi.cdef('const char *zpool_pool_state_to_name(pool_state_t);')
def zpool_pool_state_to_name(pool_state):
    """Map POOL STATE to printed strings."""
    return ffi.string(czfs.zpool_pool_state_to_name(pool_state))


#ffi.cdef('void zpool_free_handles(libzfs_handle_t *);')
def zpool_free_handles(zhp):
    return czfs.zpool_free_handles(zhp)


""" Iterate over all active pools in the system """


#ffi.cdef('typedef int (*zpool_iter_f)(zpool_handle_t *, void *);')


#ffi.cdef('int zpool_iter(libzfs_handle_t *, zpool_iter_f, void *);')
def zpool_iter(zhp, handler, arg=None):
    return czfs.zpool_iter(zhp, handler, ffi.new_handle(arg))


""" Functions to manipulate pool and vdev state """


#ffi.cdef('int zpool_clear(zpool_handle_t *, const char *, nvlist_t *);')
#def zpool_clear(zhp, blah, nvblah):
#    pass


""" Pool health statistics """


#ffi.cdef('zpool_status_t zpool_get_status(zpool_handle_t *, char **);')
def zpool_get_status(zhp, arg=None):
    """Get status of zpool"""
    return czfs.zpool_get_status(zhp, arg)


"""
Basic handle manipulations.  These functions do not create or destroy the
underlying datasets, only the references to them.
"""


#ffi.cdef('void zfs_close(zfs_handle_t *);')
def zfs_close(zhp):
    """Closes zfs_handle"""
    return czfs.zfs_close(zhp)


#ffi.cdef('zfs_handle_t *zfs_open(libzfs_handle_t *, const char *, int);')
def zfs_open(zhp, name, types_mask=sum(zfs_type_t)):
    """Gets zfs_handle for dataset"""
    return ffi.gc(czfs.zfs_open(zhp, name, types_mask), zfs_close)


#ffi.cdef('zfs_handle_t *zfs_handle_dup(zfs_handle_t *);')
def zfs_handle_dup(zhp):
    """Duplicates zfs_handle"""
    return ffi.gc(czfs.zfs_handle_dup(zhp), zfs_close)


#ffi.cdef('int zfs_get_type(const zfs_handle_t *);')
def zfs_get_type(zhp):
    """Gets type for zfs_handle"""
    return zfs_type_t[czfs.zfs_get_type(zhp)]


#ffi.cdef('const char *zfs_get_name(const zfs_handle_t *);')
def zfs_get_name(zhp):
    """Gets name for zfs_handle"""
    return ffi.string(czfs.zfs_get_name(zhp))


#ffi.cdef('zpool_handle_t *zfs_get_pool_handle(const zfs_handle_t *);')
def zfs_get_pool_handle(zhp):
    """Gets pool handle for zfs_handle"""
    return czfs.zfs_get_pool_handle(zhp)


""" Iterator functions """


#ffi.cdef('typedef int (*zfs_iter_f)(zfs_handle_t *, void *);')

#ffi.cdef('int zfs_iter_root(libzfs_handle_t *, zfs_iter_f, void *);')
def zfs_iter_root(zhp, handler, arg=None):
    return czfs.zfs_iter_root(zhp, handler, ffi.new_handle(arg))

#ffi.cdef('int zfs_iter_children(zfs_handle_t *, zfs_iter_f, void *);')
def zfs_iter_children(zhp, handler, arg=None):
    return czfs.zfs_iter_children(zhp, handler, ffi.new_handle(arg))

## TODO what is boolean_t for? Name accordingly.
#ffi.cdef('int zfs_iter_dependents(zfs_handle_t *, boolean_t, zfs_iter_f, void *);')
#def zfs_iter_dependents(zhp, b, handler, arg=None):
#    return czfs.zfs_iter_dependents(zhp, b, handler, ffi.new_handle(arg))

#ffi.cdef('int zfs_iter_filesystems(zfs_handle_t *, zfs_iter_f, void *);')
def zfs_iter_filesystems(zhp, handler, arg=None):
    return czfs.zfs_iter_filesystems(zhp, handler, ffi.new_handle(arg))

## TODO what is boolean_t for? Name accordingly.
#ffi.cdef('int zfs_iter_snapshots(zfs_handle_t *, boolean_t, zfs_iter_f, void *);')
#def zfs_iter_snapshots(zhp, b, handler, arg=None):
#    return czfs.zfs_iter_snapshots(zhp, b, handler, ffi.new_handle(arg))

#ffi.cdef('int zfs_iter_snapshots_sorted(zfs_handle_t *, zfs_iter_f, void *);')
def zfs_iter_snapshots_sorted(zhp, handler, arg=None):
    return czfs.zfs_iter_snapshots_sorted(zhp, handler, ffi.new_handle(arg))

# TODO what is const char * for? Name accordingly.
#ffi.cdef('int zfs_iter_snapspec(zfs_handle_t *, const char *, zfs_iter_f, void *);')
def zfs_iter_snapspec(zhp, c, handler, arg=None):
    return czfs.zfs_iter_snapspec(zhp, c, handler, ffi.new_handle(arg))


""" Functions to create and destroy datasets. """


#ffi.cdef('int zfs_destroy(zfs_handle_t *, boolean_t);')
def zfs_destroy(zhp, defer=True):
    return czfs.zfs_destroy(zhp, boolean_t(defer))
