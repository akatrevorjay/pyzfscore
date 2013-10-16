
import libzfs
from libzfs import *


lzh = libzfs_init()
zph = zpool_open(lzh, 'bpool')
print "lzh=%s zph=%s" % (lzh, zph)


def print_zfh(zhp):
    print "zhp_name=%s" % zfs_get_name(zhp)


@ffi.callback('zfs_iter_f')
def _zfs_iter_cb(zhp, arg=None):
    print "zhp=%s, arg=%s" % (zhp, ffi.from_handle(arg))

    print_zfh(zhp)

    print "Iterating through children"
    zfs_iter_children(zhp, _zfs_iter_cb)

    return 0


def print_zph(zhp):
    print "zhp_name=%s" % zpool_get_name(zhp)
    print "zhp_state=%s" % zpool_get_state(zhp)


@ffi.callback('zpool_iter_f')
def _zpool_iter_cb(zhp, arg=None):
    print "zhp=%s, arg=%s" % (zhp, ffi.from_handle(arg))
    print_zph(zhp)

    #print "Iterating through root datasets"
    #zfs_iter_root(zhp, _zfs_iter_cb, arg=None)

    return 0


print
print "Iterating through pools arg=None"
zpool_iter(lzh, _zpool_iter_cb)

print
print "Iterating through pools arg=0"
zpool_iter(lzh, _zpool_iter_cb, 0)


print
print "Iterating through root datasets"
zfs_iter_root(lzh, _zfs_iter_cb)

