import pyzfscore
from pyzfscore import _cffi, libzfs, zfs, libnvpair
from pyzfscore.libnvpair import *
from pyzfscore.libzfs import *
from pyzfscore.zfs import *
from pyzfscore._cffi import *


def print_zfh(zhp):
    print "zhp_name=%s" % zfs_get_name(zhp)


@libzfs.ffi.callback('zfs_iter_f')
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


@libzfs.ffi.callback('zpool_iter_f')
def _zpool_iter_cb(zhp, arg=None):
    name = zpool_get_name(zhp)
    print "pool %s: zhp=%s, arg=%s" % (name, zhp, ffi.from_handle(arg))
    #print_zph(zhp)

    #print "Iterating through root datasets"
    #zfs_iter_root(zhp, _zfs_iter_cb, arg=None)

    return 0


def test_open_zpool():
    #lzh = libzfs_init()
    zph = zpool_open(LZH, 'bpool')
    print "LZH=%s zph=%s" % (LZH, zph)
    return zph


def test_iter_pools(arg=None):
    print "Iterating through pools arg=%s" % arg
    zpool_iter(LZH, _zpool_iter_cb, arg)


def test_iter_datasets(arg=None):
    print "Iterating through root datasets"
    zfs_iter_root(LZH, _zfs_iter_cb, arg)


def test_oo_iter_pools():
    print "OO Iterating through pools"
    pools = ZPool.list()
    print pools

    #for p in pools:
    #    pf = p.to_filesystem()


def test_oo_iter_datasets():
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


