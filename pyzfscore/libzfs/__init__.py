#!/usr/bin/env python

from .. import libnvpair
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


""" Property management functions. Some functions are shared with the kernel,
and are found in sys/fs/zfs.h """


""" zpool property management """


def zpool_get_prop(zhp, prop):
    value = ffi.new('char *')
    sourcetype = ffi.new('zprop_source_t *')

    # This probably doesn't belong here..
    prop = zpool_ensure_prop(prop)

    rv = czfs.zpool_get_prop(zhp, prop,
                             value, ffi.sizeof(value),
                             sourcetype)

    if not bool(rv):
        value = ffi.string(value)
        sourcetype = zprop_source_t[sourcetype[0]]
        return (value, sourcetype)


def zpool_set_prop(zhp, prop, value):
    # TODO Check for retvals, this not bool() stuff may not actually work very well..
    return not bool(czfs.zpool_set_prop(zhp, prop, value))


def zpool_get_prop_literal(zhp, prop, literal=False):
    value = ffi.new('char *')
    sourcetype = ffi.new('zprop_source_t *')
    source = ffi.new('char *')
    literal = boolean_t(literal)

    # This probably doesn't belong here..
    prop = zpool_ensure_prop(prop)

    rv = czfs.zpool_get_prop_literal(zhp, prop,
                             value, ffi.sizeof(value),
                             sourcetype,
                             source, ffi.sizeof(source),
                             literal)
    if not bool(rv):
        value = ffi.string(value)
        sourcetype = zprop_source_t[sourcetype[0]]
        source = ffi.string(source)
        return (value, sourcetype, source)


def zpool_name_to_prop(name):
    return czfs.zpool_name_to_prop(name)


def zpool_ensure_prop(name_or_prop):
    """ Convert prop to prop type int if needed """
    if isinstance(name_or_prop, basestring):
        name_or_prop = czfs.zpool_name_to_prop(name_or_prop)
    return name_or_prop


def zpool_prop_readonly(prop):
    prop = zpool_ensure_prop(prop)
    return bool(czfs.zpool_prop_readonly(prop))


""" zfs dataset property management """


def zfs_prop_get(zhp, prop, literal=False):
    value = ffi.new('char *')
    sourcetype = ffi.new('zprop_source_t *')
    source = ffi.new('char *')
    literal = boolean_t(literal)

    # This probably doesn't belong here..
    prop = zfs_ensure_prop(prop)

    rv = czfs.zfs_prop_get(zhp, prop,
                           value, ffi.sizeof(value),
                           sourcetype,
                           source, ffi.sizeof(source),
                           literal)
    if not bool(rv):
        value = ffi.string(value)
        sourcetype = zprop_source_t[sourcetype[0]]
        source = ffi.string(source)
        return (value, sourcetype, source)


def zfs_prop_set(zhp, prop, value):
    # TODO Check for retvals, this not bool() stuff may not actually work very well..
    # czfs.EZFS_MOUNTFAILED == 'property may be set, but unable to remount'
    # czfs.EZFS_SHARENFSFAILED == 'property may be set, but unable to reshare'
    # MAYBE czfs.EZFS_SHARESMBFAILED == 'property may be set, but unable to reshare'
    return not bool(czfs.zfs_prop_set(zhp, prop, value))


def zfs_get_user_props(zhp):
    return czfs.zfs_get_user_props(zhp)


# TODO Temporary, not needed
def zfs_get_user_props_dump(zhp):
    nv = zfs_get_user_props(zhp)
    return libnvpair.dump_nvlist(nv, 0)


# TODO Is this needed?
def zfs_get_user_prop(zhp, name):
    nvl = zfs_get_user_props(zhp)
    nvl = libnvpair.NVList.from_nvlist_p(nvl)

    nvp = nvl.lookup_nvlist(name)
    if not nvp:
        return

    value = nvp.lookup_string('value')
    source = nvp.lookup_string('source')

    if source == zfs_get_name(zhp):
        sourcetype = zprop_source_t.ZPROP_SRC_LOCAL
    # TODO what is the value for received user prop?
    # It's $recvd in sys/fs/zfs.h
    #elif source == '$recv':
    else:
        sourcetype = zprop_source_t.ZPROP_SRC_INHERITED

    return (value, sourcetype, source)


# TODO move this
def zfs_prop_user(propname):
    return bool(czfs.zfs_prop_user(propname))


def zfs_name_to_prop(name):
    return czfs.zfs_name_to_prop(name)


def zfs_ensure_prop(name_or_prop):
    """ Convert prop to prop type int if needed """
    if isinstance(name_or_prop, basestring):
        name_or_prop = czfs.zfs_name_to_prop(name_or_prop)
    return name_or_prop


def zfs_prop_readonly(prop):
    prop = zfs_ensure_prop(prop)
    return bool(czfs.zfs_prop_readonly(prop))


def zfs_prop_inheritable(prop):
    prop = zfs_ensure_prop(prop)
    return bool(czfs.zfs_prop_inheritable(prop))


def zfs_prop_inherit(zhp, propname, received=False):
    received = boolean_t(received)
    rv = czfs.zfs_prop_inherit(zhp, propname, received)
    return not bool(rv)


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
    bt_defer = boolean_t(defer)
    return not bool(czfs.zfs_destroy(zhp, bt_defer))


def zfs_destroy_snaps(zhp, snapname, defer=True):
    """Destroys all snapshost with given name in zhp & descendants."""
    bt_defer = boolean_t(defer)
    return not bool(czfs.zfs_destroy_snaps(zhp, snapname, bt_defer))


def zfs_snapshot(lzh, path, recursive=False, props=None):
    nvl_props = libnvpair.NVList()
    nvl_props.update(props)
    bt_recursive = boolean_t(recursive)
    return not bool(czfs.zfs_snapshot(lzh, path, bt_recursive, nvl_props.handle[0]))


""" Miscellaneous functions. """


def zfs_type_to_name(zfs_type_t):
    return ffi.string(czfs.zfs_type_to_name(zfs_type_t))


def zfs_refresh_properties(zhp):
    return czfs.zfs_refresh_properties(zhp)


def zfs_name_valid(name, zfs_type_t=zfs_type_t.ALL):
    return czfs.zfs_name_valid(name, zfs_type_t)


def zfs_dataset_exists(zhp, name, zfs_type_t=zfs_type_t.ALL):
    """Returns if dataset @name exists."""
    return bool(czfs.zfs_dataset_exists(zhp, name, zfs_type_t))


""" Mount support functions. """


def zfs_is_mounted(zhp):
    """If @zfs_handle:zhp is mounted, return path where"""
    where = ffi.new('char **')
    ret = czfs.zfs_is_mounted(zhp, where)
    if ret:
        return ffi.string(where[0])
