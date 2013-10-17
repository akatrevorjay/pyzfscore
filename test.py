
import libzfs
from libzfs import *
import zfs
from zfs import *


#lzh = libzfs_init()
#zph = zpool_open(lzh, 'bpool')
#print "lzh=%s zph=%s" % (lzh, zph)


def print_zfh(zhp):
    print "zhp_name=%s" % zfs_get_name(zhp)


@ffi.callback('zfs_iter_f')
def _zfs_iter_cb(zhp, arg=None):
    arg = ffi.from_handle(arg)
    name = zfs_get_name(zhp)
    print "%s: zhp=%s, arg=%s" % (name, zhp, arg)
    #print_zfh(zhp)

    if arg != 'noiter':
        #print "%s: Iterating through children" % name
        #zfs_iter_children(zhp, _zfs_iter_cb)

        print "%s: Iterating through filesystems" % name
        zfs_iter_filesystems(zhp, _zfs_iter_cb)

        print "%s: Iterating through snapshots sorted" % name
        zfs_iter_snapshots_sorted(zhp, _zfs_iter_cb, 'noiter')

    return 0


def print_zph(zhp):
    print "zhp_name=%s" % zpool_get_name(zhp)
    print "zhp_state=%s" % zpool_get_state(zhp)


@ffi.callback('zpool_iter_f')
def _zpool_iter_cb(zhp, arg=None):
    name = zpool_get_name(zhp)
    print "pool %s: zhp=%s, arg=%s" % (name, zhp, ffi.from_handle(arg))
    #print_zph(zhp)

    #print "Iterating through root datasets"
    #zfs_iter_root(zhp, _zfs_iter_cb, arg=None)

    return 0


#print
#print "Iterating through pools arg=None"
#zpool_iter(lzh, _zpool_iter_cb)

#print
#print "Iterating through pools arg=0"
#zpool_iter(lzh, _zpool_iter_cb, 0)


#print
#print "Iterating through root datasets"
#zfs_iter_root(lzh, _zfs_iter_cb)


print
print "OO Iterating through pools"

pools = ZPool.list()
print pools

#for p in pools:
#    pf = p.to_filesystem()

print
print "OO Iterating through datasets"

datasets = ZDataset.iter_root()
print datasets

for dataset in datasets:
    print "%s: Iterating children" % dataset
    print dataset.iter_children()

    print "%s: Iterating filesystems" % dataset
    print dataset.iter_filesystems()

    print "%s: Iterating snapshots sorted" % dataset
    print dataset.iter_snapshots_sorted()


