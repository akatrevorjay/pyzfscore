
from .._cffi import ffi, cdef, ptop
from ..flufl.enum import IntEnum


class libzfs_errors(IntEnum):
    EZFS_NOMEM = 2000  # Out of memory
    EZFS_BADPROP = 2001  # Invalid property value
    EZFS_PROPREADONLY = 2002  # cannot set readonly property
    EZFS_PROPTYPE = 2003  # property does not apply to dataset type
    EZFS_PROPNONINHERIT = 2004  # property is not inheritable
    EZFS_PROPSPACE = 2005  # bad quota or reservation
    EZFS_BADTYPE = 2006  # dataset is not of appropriate type
    EZFS_BUSY = 2007  # pool or dataset is busy
    EZFS_EXISTS = 2008  # pool or dataset already exists
    EZFS_NOENT = 2009  # no such pool or dataset
    EZFS_BADSTREAM = 2010  # bad backup stream
    EZFS_DSREADONLY = 2011  # dataset is readonly
    EZFS_VOLTOOBIG = 2012  # volume is too large for 32-bit system
    EZFS_INVALIDNAME = 2013  # invalid dataset name
    EZFS_BADRESTORE = 2014  # unable to restore to destination
    EZFS_BADBACKUP = 2015  # backup failed
    EZFS_BADTARGET = 2016  # bad attach/detach/replace target
    EZFS_NODEVICE = 2017  # no such device in pool
    EZFS_BADDEV = 2018  # invalid device to add
    EZFS_NOREPLICAS = 2019  # no valid replicas
    EZFS_RESILVERING = 2020  # currently resilvering
    EZFS_BADVERSION = 2021  # unsupported version
    EZFS_POOLUNAVAIL = 2022  # pool is currently unavailable
    EZFS_DEVOVERFLOW = 2023  # too many devices in one vdev
    EZFS_BADPATH = 2024  # must be an absolute path
    EZFS_CROSSTARGET = 2025  # rename or clone across pool or dataset
    EZFS_ZONED = 2026  # used improperly in local zone
    EZFS_MOUNTFAILED = 2027  # failed to mount dataset
    EZFS_UMOUNTFAILED = 2028  # failed to unmount dataset
    EZFS_UNSHARENFSFAILED = 2029  # unshare(1M) failed
    EZFS_SHARENFSFAILED = 2030  # share(1M) failed
    EZFS_PERM = 2031  # permission denied
    EZFS_NOSPC = 2032  # out of space
    EZFS_FAULT = 2033  # bad address
    EZFS_IO = 2034  # I/O error
    EZFS_INTR = 2035  # signal received
    EZFS_ISSPARE = 2036  # device is a hot spare
    EZFS_INVALCONFIG = 2037  # invalid vdev configuration
    EZFS_RECURSIVE = 2038  # recursive dependency
    EZFS_NOHISTORY = 2039  # no history object
    EZFS_POOLPROPS = 2040  # couldn't retrieve pool props
    EZFS_POOL_NOTSUP = 2041  # ops not supported for this type of pool
    EZFS_POOL_INVALARG = 2042  # invalid argument for this pool operation
    EZFS_NAMETOOLONG = 2043  # dataset name is too long
    EZFS_OPENFAILED = 2044  # open of device failed
    EZFS_NOCAP = 2045  # couldn't get capacity
    EZFS_LABELFAILED = 2046  # write of label failed
    EZFS_BADWHO = 2047  # invalid permission who
    EZFS_BADPERM = 2048  # invalid permission
    EZFS_BADPERMSET = 2049  # invalid permission set name
    EZFS_NODELEGATION = 2050  # delegated administration is disabled
    EZFS_UNSHARESMBFAILED = 2051  # failed to unshare over smb
    EZFS_SHARESMBFAILED = 2052  # failed to share over smb
    EZFS_BADCACHE = 2053  # bad cache file
    EZFS_ISL2CACHE = 2054  # device is for the level 2 ARC
    EZFS_VDEVNOTSUP = 2055  # unsupported vdev type
    EZFS_NOTSUP = 2056  # ops not supported on this dataset
    EZFS_ACTIVE_SPARE = 2057  # pool has active shared spare devices
    EZFS_UNPLAYED_LOGS = 2058  # log device has unplayed logs
    EZFS_REFTAG_RELE = 2059  # snapshot release: tag not found
    EZFS_REFTAG_HOLD = 2060  # snapshot hold: tag already exists
    EZFS_TAGTOOLONG = 2061  # snapshot hold/rele: tag too long
    EZFS_PIPEFAILED = 2062  # pipe create failed
    EZFS_THREADCREATEFAILED = 2063  # thread create failed
    EZFS_POSTSPLIT_ONLINE = 2064  # onlining a disk after splitting it
    EZFS_SCRUBBING = 2065  # currently scrubbing
    EZFS_NO_SCRUB = 2066  # no active scrub
    EZFS_DIFF = 2067  # general failure of zfs diff
    EZFS_DIFFDATA = 2068  # bad zfs diff data
    EZFS_POOLREADONLY = 2069  # pool is in read-only mode
    EZFS_KEYERR = 2070  # crypto key not present or invalid
    EZFS_UNKNOWN = 2071


class zfs_type_t(IntEnum):
    """ Each dataset can be one of the following types.  These constants can be
    combined into masks that can be passed to various functions. """
    ZFS_TYPE_FILESYSTEM = 1
    ZFS_TYPE_SNAPSHOT = 2
    ZFS_TYPE_VOLUME = 4
    ZFS_TYPE_POOL = 8


class zfs_prop_t(IntEnum):
    ZFS_NUM_PROPS = 63
    ZFS_PROP_ACLINHERIT = 25
    ZFS_PROP_ATIME = 17
    ZFS_PROP_AVAILABLE = 3
    ZFS_PROP_CANMOUNT = 28
    ZFS_PROP_CASE = 36
    ZFS_PROP_CHECKSUM = 15
    ZFS_PROP_CLONES = 61
    ZFS_PROP_COMPRESSION = 16
    ZFS_PROP_COMPRESSRATIO = 5
    ZFS_PROP_COPIES = 32
    ZFS_PROP_CREATETXG = 26
    ZFS_PROP_CREATION = 1
    ZFS_PROP_DEDUP = 56
    ZFS_PROP_DEFER_DESTROY = 51
    ZFS_PROP_DEVICES = 18
    ZFS_PROP_EXEC = 19
    ZFS_PROP_GUID = 42
    ZFS_PROP_ISCSIOPTIONS = 29
    ZFS_PROP_LOGBIAS = 53
    ZFS_PROP_MLSLABEL = 57
    ZFS_PROP_MOUNTED = 6
    ZFS_PROP_MOUNTPOINT = 13
    ZFS_PROP_NAME = 27
    ZFS_PROP_NBMAND = 38
    ZFS_PROP_NORMALIZE = 35
    ZFS_PROP_NUMCLONES = 31
    ZFS_PROP_OBJSETID = 55
    ZFS_PROP_ORIGIN = 7
    ZFS_PROP_PRIMARYCACHE = 43
    ZFS_PROP_PRIVATE = 24
    ZFS_PROP_QUOTA = 8
    ZFS_PROP_READONLY = 21
    ZFS_PROP_RECORDSIZE = 12
    ZFS_PROP_REFERENCED = 4
    ZFS_PROP_REFQUOTA = 40
    ZFS_PROP_REFRATIO = 59
    ZFS_PROP_REFRESERVATION = 41
    ZFS_PROP_RESERVATION = 9
    ZFS_PROP_SECONDARYCACHE = 44
    ZFS_PROP_SETUID = 20
    ZFS_PROP_SHARENFS = 14
    ZFS_PROP_SHARESMB = 39
    ZFS_PROP_SNAPDEV = 62
    ZFS_PROP_SNAPDIR = 23
    ZFS_PROP_STMF_SHAREINFO = 50
    ZFS_PROP_SYNC = 58
    ZFS_PROP_TYPE = 0
    ZFS_PROP_UNIQUE = 54
    ZFS_PROP_USED = 2
    ZFS_PROP_USEDCHILD = 47
    ZFS_PROP_USEDDS = 46
    ZFS_PROP_USEDREFRESERV = 48
    ZFS_PROP_USEDSNAP = 45
    ZFS_PROP_USERACCOUNTING = 49
    ZFS_PROP_USERREFS = 52
    ZFS_PROP_UTF8ONLY = 34
    ZFS_PROP_VERSION = 33
    ZFS_PROP_VOLBLOCKSIZE = 11
    ZFS_PROP_VOLSIZE = 10
    ZFS_PROP_VSCAN = 37
    ZFS_PROP_WRITTEN = 60
    ZFS_PROP_XATTR = 30
    ZFS_PROP_ZONED = 22


class zfs_userquota_prop_t(IntEnum):
    ZFS_PROP_USERUSED = 0
    ZFS_PROP_USERQUOTA = 1
    ZFS_PROP_GROUPUSED = 2
    ZFS_PROP_GROUPQUOTA = 3
    ZFS_NUM_USERQUOTA_PROPS = 4


class zpool_prop_t(IntEnum):
    ZPOOL_PROP_NAME = 0
    ZPOOL_PROP_SIZE = 1
    ZPOOL_PROP_CAPACITY = 2
    ZPOOL_PROP_ALTROOT = 3
    ZPOOL_PROP_HEALTH = 4
    ZPOOL_PROP_GUID = 5
    ZPOOL_PROP_VERSION = 6
    ZPOOL_PROP_BOOTFS = 7
    ZPOOL_PROP_DELEGATION = 8
    ZPOOL_PROP_AUTOREPLACE = 9
    ZPOOL_PROP_CACHEFILE = 10
    ZPOOL_PROP_FAILUREMODE = 11
    ZPOOL_PROP_LISTSNAPS = 12
    ZPOOL_PROP_AUTOEXPAND = 13
    ZPOOL_PROP_DEDUPDITTO = 14
    ZPOOL_PROP_DEDUPRATIO = 15
    ZPOOL_PROP_FREE = 16
    ZPOOL_PROP_ALLOCATED = 17
    ZPOOL_PROP_READONLY = 18
    ZPOOL_PROP_ASHIFT = 19
    ZPOOL_PROP_COMMENT = 20
    ZPOOL_PROP_EXPANDSZ = 21
    ZPOOL_PROP_FREEING = 22
    ZPOOL_NUM_PROPS = 23


class zprop_source_t(IntEnum):
    ZPROP_SRC_NONE = 0x1
    ZPROP_SRC_DEFAULT = 0x2
    ZPROP_SRC_TEMPORARY = 0x4
    ZPROP_SRC_LOCAL = 0x8
    ZPROP_SRC_INHERITED = 0x10
    ZPROP_SRC_RECEIVED = 0x20


zpool_status_t = IntEnum('zpool_status_t', [
    # The following correspond to faults as defined in the (fault.fs.zfs.)
    # event namespace.  Each is associated with a corresponding message ID.
    'ZPOOL_STATUS_CORRUPT_CACHE',    # corrupt /kernel/drv/zpool.cache
    'ZPOOL_STATUS_MISSING_DEV_R',    # missing device with replicas
    'ZPOOL_STATUS_MISSING_DEV_NR',    # missing device with no replicas
    'ZPOOL_STATUS_CORRUPT_LABEL_R',    # bad device label with replicas
    'ZPOOL_STATUS_CORRUPT_LABEL_NR',    # bad device label with no replicas
    'ZPOOL_STATUS_BAD_GUID_SUM',    # sum of device guids didn't match
    'ZPOOL_STATUS_CORRUPT_POOL',    # pool metadata is corrupted
    'ZPOOL_STATUS_CORRUPT_DATA',    # data errors in user (meta)data
    'ZPOOL_STATUS_FAILING_DEV',    # device experiencing errors
    'ZPOOL_STATUS_VERSION_NEWER',    # newer on-disk version
    'ZPOOL_STATUS_HOSTID_MISMATCH',    # last accessed by another system
    'ZPOOL_STATUS_IO_FAILURE_WAIT',    # failed I/O, failmode 'wait'
    'ZPOOL_STATUS_IO_FAILURE_CONTINUE',  # failed I/O, failmode 'continue'
    'ZPOOL_STATUS_BAD_LOG',        # cannot read log chain(s)

    # If the pool has unsupported features but can still be opened in
    # read-only mode, its status is ZPOOL_STATUS_UNSUP_FEAT_WRITE. If the
    # pool has unsupported features but cannot be opened at all, its
    # status is ZPOOL_STATUS_UNSUP_FEAT_READ.
    'ZPOOL_STATUS_UNSUP_FEAT_READ',    # unsupported features for read
    'ZPOOL_STATUS_UNSUP_FEAT_WRITE',    # unsupported features for write

    # These faults have no corresponding message ID.  At the time we are
    # checking the status, the original reason for the FMA fault (I/O or
    # checksum errors) has been lost.
    'ZPOOL_STATUS_FAULTED_DEV_R',    # faulted device with replicas
    'ZPOOL_STATUS_FAULTED_DEV_NR',    # faulted device with no replicas

    # The following are not faults per se, but still an error possibly
    # requiring administrative attention.  There is no corresponding
    # message ID.
    'ZPOOL_STATUS_VERSION_OLDER',    # older legacy on-disk version
    'ZPOOL_STATUS_FEAT_DISABLED',    # supported features are disabled
    'ZPOOL_STATUS_RESILVERING',    # device being resilvered
    'ZPOOL_STATUS_OFFLINE_DEV',    # device online
    'ZPOOL_STATUS_REMOVED_DEV',    # removed device

    # Finally, the following indicates a healthy pool.
    'ZPOOL_STATUS_OK',
    ], start=0)


""" C defs """


cdef('''
typedef struct { ...; } zfs_perm_node_t;
typedef struct { ...; } zfs_allow_node_t;
typedef struct { ...; } zfs_allow_t;
''')


cdef('''
typedef ... zfs_handle_t;
typedef ... zpool_handle_t;
typedef ... libzfs_handle_t;
''')


""" Types """


cdef('typedef enum { B_FALSE, B_TRUE } boolean_t;')

def boolean_t(value=None):
    return ffi.cast('boolean_t', value)


