
import ctypes as C
from ctypes import *

from libnvpair import *

from cfunc import *
from cstruct import *
from enum import *

from anodi import returns, annotated, empty


def register_type(*args, **kwargs):
    def _register(k, v=None):
        if v is None:
            v = k
        if isinstance(v, basestring):
            v = globals()[v]
        C_struct.register_type(k, v)
        #C_function.register_type(k, v)
    for arg in args:
        _register(arg)
    for k, v in kwargs:
        _register(k, v)

#register_type('nvlist_p', 'nvlist_t')


def _cmeth_bakery(what, argtypes=None, restype=None):
    ret = what
    if argtypes:
        ret.argtypes = argtypes
    if restype:
        ret.restype = restype
    return ret


class libzfs_errors(Enumeration):
    #_members_start_ = 2000
    #_members_ = []
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


MAXNAMELEN = 256
ZFS_MAXNAMELEN = MAXNAMELEN


@C_struct()
class zfs_handle_t:
    zfs_name = c_char * ZFS_MAXNAMELEN


zfs_handle_ptr = POINTER(zfs_handle_t)


@C_struct()
class zpool_handle_t:
    zpool_name = c_char * ZFS_MAXNAMELEN
    zpool_state = c_int
    zpool_config = nvlist_p
    zpool_old_config = nvlist_p
    zpool_props = nvlist_p


zpool_handle_ptr = POINTER(zpool_handle_t)


@C_struct()
class libzfs_handle_t:
    libzfs_log_str = c_char_p
    libzfs_action = c_char * 1024
    libzfs_desc_active = c_int
    libzfs_desc = c_char * 1024
    libzfs_printerr = c_int
    libzfs_storeerr = c_int


libzfs_handle_ptr = POINTER(libzfs_handle_t)

lz = CDLL("libzfs.so")


#
# Library initialization
#


# libzfs_handle_t *libzfs_init(void);
@C_function(lz)
@returns(libzfs_handle_ptr)
def libzfs_init():
    return libzfs_init.c_function()


# void libzfs_fini(libzfs_handle_t *);
@C_function(lz)
@annotated(returns=None)
def libzfs_fini(zh=(libzfs_handle_ptr,)):
    return libzfs_fini.c_function(zh)


# libzfs_handle_t *zpool_get_handle(zpool_handle_t *);
zpool_get_handle = _cmeth_bakery(
    lz.zpool_get_handle,
    argtypes=[zpool_handle_ptr],
    restype=libzfs_handle_ptr,
)


# libzfs_handle_t *zfs_get_handle(zfs_handle_t *);
zfs_get_handle = _cmeth_bakery(
    lz.zfs_get_handle,
    argtypes=[zfs_handle_ptr],
    restype=libzfs_handle_ptr,
)

# void libzfs_print_on_error(libzfs_handle_t *, boolean_t);
libzfs_print_on_error = _cmeth_bakery(
    lz.libzfs_print_on_error,
    argtypes=[libzfs_handle_ptr, c_bool],
    restype=None,
)

# int libzfs_errno(libzfs_handle_t *);
libzfs_errno = _cmeth_bakery(
    lz.libzfs_errno,
    argtypes=[libzfs_handle_ptr],
    restype=c_int,
)

# const char *libzfs_error_action(libzfs_handle_t *);
libzfs_error_action = _cmeth_bakery(
    lz.libzfs_error_action,
    argtypes=[libzfs_handle_ptr],
    restype=c_char_p,
)

# const char *libzfs_error_description(libzfs_handle_t *);
libzfs_error_description = _cmeth_bakery(
    lz.libzfs_error_description,
    argtypes=[libzfs_handle_ptr],
    restype=c_char_p,
)

# void libzfs_mnttab_init(libzfs_handle_t *);
#libzfs_mnttab_init = lz.libzfs_mnttab_init
#libzfs_mnttab_init.argtypes = [libzfs_handle_ptr]
#libzfs_mnttab_init.restype = None

# void libzfs_mnttab_fini(libzfs_handle_t *);
#libzfs_mnttab_fini = lz.libzfs_mnttab_fini
#libzfs_mnttab_fini.argtypes = [libzfs_handle_ptr]
#libzfs_mnttab_fini.restype = None

# void libzfs_mnttab_cache(libzfs_handle_t *, boolean_t);
#libzfs_mnttab_cache = lz.libzfs_mnttab_cache

# int libzfs_mnttab_find(libzfs_handle_t *, const char *, struct mnttab *);
#libzfs_mnttab_find = lz.libzfs_mnttab_find

# void libzfs_mnttab_add(libzfs_handle_t *, const char *, const char *, const char *);
#libzfs_mnttab_add = lz.libzfs_mnttab_add

# void libzfs_mnttab_remove(libzfs_handle_t *, const char *);
#libzfs_mnttab_remove = lz.libzfs_mnttab_remove


#
# Zfs Basic
#

zfs_open = _cmeth_bakery(
    lz.zfs_open,
    argtypes=[libzfs_handle_ptr, c_char_p, c_int],
    restype=zfs_handle_ptr,
)

zfs_handle_dup = _cmeth_bakery(
    lz.zfs_handle_dup,
    argtypes=[libzfs_handle_ptr, zfs_handle_ptr],
    restype=zfs_handle_ptr,
)

zfs_close = _cmeth_bakery(
    lz.zfs_close,
    argtypes=[zfs_handle_ptr],
    restype=None,
)


class zfs_type_t(Enumeration):
    """ Each dataset can be one of the following types.  These constants can be
    combined into masks that can be passed to various functions. """
    ZFS_TYPE_FILESYSTEM = 1
    ZFS_TYPE_SNAPSHOT = 2
    ZFS_TYPE_VOLUME = 4
    ZFS_TYPE_POOL = 8

zfs_type_ptr = POINTER(zfs_type_t)


zfs_get_type = _cmeth_bakery(
    lz.zfs_get_type,
    argtypes=[zfs_handle_ptr],
    restype=zfs_type_t,
)

zfs_get_name = _cmeth_bakery(
    lz.zfs_get_name,
    argtypes=[zfs_handle_ptr],
    restype=c_char_p,
)

zfs_get_pool_handle = _cmeth_bakery(
    lz.zfs_get_pool_handle,
    argtypes=[zfs_handle_ptr],
    restype=zpool_handle_ptr,
)


#
# Property management
#


class zfs_prop_t(Enumeration):
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

zfs_prop_ptr = POINTER(zfs_prop_t)


class zfs_userquota_prop_t(Enumeration):
    ZFS_PROP_USERUSED = 0
    ZFS_PROP_USERQUOTA = 1
    ZFS_PROP_GROUPUSED = 2
    ZFS_PROP_GROUPQUOTA = 3
    ZFS_NUM_USERQUOTA_PROPS = 4

zfs_userquota_prop_ptr = POINTER(zfs_userquota_prop_t)


class zpool_prop_t(Enumeration):
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

zpool_prop_ptr = POINTER(zpool_prop_t)


class zprop_source_t(Enumeration):
    ZPROP_SRC_NONE = 0x1
    ZPROP_SRC_DEFAULT = 0x2
    ZPROP_SRC_TEMPORARY = 0x4
    ZPROP_SRC_LOCAL = 0x8
    ZPROP_SRC_INHERITED = 0x10
    ZPROP_SRC_RECEIVED = 0x20

zprop_source_ptr = POINTER(zprop_source_t)


# extern uint64_t zfs_prop_default_numeric(zfs_prop_t);
zfs_prop_default_numeric = _cmeth_bakery(
    lz.zfs_prop_default_numeric,
    argtypes=[zfs_prop_t],
    restype=c_int,
)


zfs_prop_default_string = _cmeth_bakery(
    lz.zfs_prop_default_string,
    argtypes=[zfs_prop_t],
    restype=c_char_p,
)


#extern const char *zfs_prop_column_name(zfs_prop_t);
zfs_prop_column_name = _cmeth_bakery(
    lz.zfs_prop_column_name,
    argtypes=[zfs_prop_t],
    restype=c_char_p,
)


#extern boolean_t zfs_prop_align_right(zfs_prop_t);
zfs_prop_align_right = _cmeth_bakery(
    lz.zfs_prop_align_right,
    argtypes=[zfs_prop_t],
    restype=c_bool,
)


#extern nvlist_t *zfs_valid_proplist(libzfs_handle_t *, zfs_type_t,
#    nvlist_t *, uint64_t, zfs_handle_t *, const char *);

#extern const char *zfs_prop_to_name(zfs_prop_t);

#extern int zfs_prop_set(zfs_handle_t *, const char *, const char *);
zfs_prop_set = _cmeth_bakery(
    lz.zfs_prop_set,
    argtypes=[zfs_handle_ptr, c_char_p, c_char_p],
    restype=c_int,
)


#extern int zfs_prop_get(zfs_handle_t *, zfs_prop_t, char *, size_t,
#    zprop_source_t *, char *, size_t, boolean_t);
zfs_prop_get = _cmeth_bakery(
    lz.zfs_prop_get,
    argtypes=[
        zfs_handle_ptr,
        zfs_prop_t, c_char_p, c_size_t,
        zprop_source_ptr, c_char_p, c_size_t,
        c_bool,
    ],
    restype=c_int,
)


#extern int zfs_prop_get_recvd(zfs_handle_t *, const char *, char *, size_t,
#    boolean_t);
zfs_prop_get_recvd = _cmeth_bakery(
    lz.zfs_prop_get_recvd,
    argtypes=[
        zfs_handle_ptr,
        c_char_p, c_char_p, c_size_t,
        c_bool,
    ],
    restype=c_int,
)


#extern int zfs_prop_get_numeric(zfs_handle_t *, zfs_prop_t, uint64_t *,
#    zprop_source_t *, char *, size_t);
zfs_prop_get_numeric = _cmeth_bakery(
    lz.zfs_prop_get_numeric,
    argtypes=[
        zfs_handle_ptr,
        zfs_prop_t, c_int_p,
        zprop_source_ptr, c_char_p, c_size_t,
    ],
    restype=c_int,
)


#extern int zfs_prop_get_userquota_int(zfs_handle_t *zhp, const char *propname,
#    uint64_t *propvalue);
#extern int zfs_prop_get_userquota(zfs_handle_t *zhp, const char *propname,
#    char *propbuf, int proplen, boolean_t literal);
# extern int zfs_prop_get_written_int(zfs_handle_t *zhp, const char *propname,
#    uint64_t *propvalue);
zfs_prop_get_written_int = _cmeth_bakery(
    lz.zfs_prop_get_written_int,
    argtypes=[zfs_handle_ptr, c_char_p, c_int_p],
    restype=c_int,
)

# extern int zfs_prop_get_written(zfs_handle_t *zhp, const char *propname,
#     char *propbuf, int proplen, boolean_t literal);
zfs_prop_get_written = _cmeth_bakery(
    lz.zfs_prop_get_written,
    argtypes=[zfs_handle_ptr, c_char_p, c_char_p, c_int, c_bool],
    restype=c_int,
)


#extern int zfs_prop_get_feature(zfs_handle_t *zhp, const char *propname,
#    char *buf, size_t len);
#extern int zfs_get_snapused_int(zfs_handle_t *firstsnap, zfs_handle_t *lastsnap,
#    uint64_t *usedp);
#extern uint64_t getprop_uint64(zfs_handle_t *, zfs_prop_t, char **);
#extern uint64_t zfs_prop_get_int(zfs_handle_t *, zfs_prop_t);
zfs_prop_get_int = _cmeth_bakery(
    lz.zfs_prop_get_int,
    argtypes=[zfs_handle_ptr, zfs_prop_t],
    restype=c_int,
)


#extern int zfs_prop_inherit(zfs_handle_t *, const char *, boolean_t);
zfs_prop_inherit = _cmeth_bakery(
    lz.zfs_prop_inherit,
    argtypes=[zfs_handle_ptr, c_char_p, c_bool],
    restype=c_int,
)


#extern const char *zfs_prop_values(zfs_prop_t);
zfs_prop_values = _cmeth_bakery(
    lz.zfs_prop_values,
    argtypes=[zfs_prop_t],
    restype=c_char_p,
)


#extern int zfs_prop_is_string(zfs_prop_t prop);
zfs_prop_is_string = _cmeth_bakery(
    lz.zfs_prop_is_string,
    argtypes=[zfs_prop_t],
    restype=c_int,
)


#extern nvlist_t *zfs_get_user_props(zfs_handle_t *);
zfs_get_user_props = _cmeth_bakery(
    lz.zfs_get_user_props,
    argtypes=[
        zfs_handle_ptr,
    ],
    restype=nvlist_p,
)


#extern nvlist_t *zfs_get_recvd_props(zfs_handle_t *);
#zfs_get_recvd_props = _cmeth_bakery(
#    lz.zfs_get_recvd_props,
#    argtypes=[
#        zfs_handle_ptr,
#    ],
#    restype=nvlist_p,
#)


#extern nvlist_t *zfs_get_clones_nvl(zfs_handle_t *);
zfs_get_clones_nvl = _cmeth_bakery(
    lz.zfs_get_clones_nvl,
    argtypes=[
        zfs_handle_ptr,
    ],
    restype=nvlist_p,
)


@C_struct()
class zprop_list_t:
    pl_prop = c_int
    pl_user_prop = c_char_p
    pl_all = c_bool
    pl_width = c_size_t
    pl_recvd_width = c_size_t
    pl_fixed = c_bool

zprop_list_t.pl_next = zprop_list_t

zprop_list_ptr = C.POINTER(zprop_list_t)
zprop_list_pp = C.POINTER(zprop_list_ptr)


#extern int zfs_expand_proplist(zfs_handle_t *, zprop_list_t **, boolean_t);
@C_function(lz)
@annotated(returns=c_int)
def zfs_expand_proplist(
    zfsh=(zfs_handle_ptr, ),
    prop_list=(zprop_list_pp, ),
    boolean=(c_bool, ),
):
    return zfs_expand_proplist.c_function(zfsh, prop_list, boolean)


#extern void zfs_prune_proplist(zfs_handle_t *, uint8_t *);
@C_function(lz)
@annotated(returns=None)
def zfs_prune_proplist(
    zfsh=(zfs_handle_ptr, ),
    uint8_t=(c_int_p, ),
):
    return zfs_prune_proplist.c_function(zfsh, uint8_t)

##define	ZFS_MOUNTPOINT_NONE	"none"
##define	ZFS_MOUNTPOINT_LEGACY	"legacy"

##define	ZFS_FEATURE_DISABLED	"disabled"
##define	ZFS_FEATURE_ENABLED	"enabled"
##define	ZFS_FEATURE_ACTIVE	"active"

##define	ZFS_UNSUPPORTED_INACTIVE	"inactive"
##define	ZFS_UNSUPPORTED_READONLY	"readonly"


#
# Basic handle functions
#


# zpool_handle_t *zpool_open(libzfs_handle_t *, const char *);
zpool_open = _cmeth_bakery(
    lz.zpool_open,
    argtypes=[libzfs_handle_ptr, c_char_p],
    restype=zpool_handle_ptr,
)

# zpool_handle_t *zpool_open_canfail(libzfs_handle_t *, const char *);
zpool_open_canfail = _cmeth_bakery(
    lz.zpool_open_canfail,
    argtypes=[libzfs_handle_ptr, c_char_p],
    restype=zpool_handle_ptr,
)

# void zpool_close(zpool_handle_t *);
zpool_close = _cmeth_bakery(
    lz.zpool_close,
    argtypes=[zpool_handle_ptr],
)

# const char *zpool_get_name(zpool_handle_t *);
zpool_get_name = _cmeth_bakery(
    lz.zpool_get_name,
    argtypes=[zpool_handle_ptr],
    restype=c_char_p,
)

# int zpool_get_state(zpool_handle_t *);
zpool_get_state = _cmeth_bakery(
    lz.zpool_get_state,
    argtypes=[zpool_handle_ptr],
    restype=c_int,
)

# char *zpool_state_to_name(vdev_state_t, vdev_aux_t);
zpool_state_to_name = _cmeth_bakery(
    lz.zpool_state_to_name,
    argtypes=[zpool_handle_ptr],
    restype=c_char_p,
)

# void zpool_free_handles(libzfs_handle_t *);
zpool_free_handles = _cmeth_bakery(
    lz.zpool_free_handles,
    argtypes=[libzfs_handle_ptr],
)


#
# Pool Iteration
#


# Callback function prototype
# typedef int (*zpool_iter_f)(zpool_handle_t *, void *);
ZPOOL_ITER_CALLBACK_PROTOTYPE = CFUNCTYPE(c_int, zpool_handle_ptr, c_void_p)


# extern int zpool_iter(libzfs_handle_t *, zpool_iter_f, void *);
@C_function(lz)
@annotated(returns=c_int)
def zpool_iter(zh=(libzfs_handle_ptr, ),
               callback=(ZPOOL_ITER_CALLBACK_PROTOTYPE, None),
               void=(c_void_p, None),
               ):
    """ Iterate over all active pools in the system. """
    if callback is None:
        callback = _zpool_iter_callback_example
    return zpool_iter.c_function(zh, callback, void)


def __zpool_iter_callback_example(zph, void):
    """ Example zpool_iter callback function that just prints data """
    name = zpool_get_name(zph)
    print "zph=%s void=%s name=%s" % (zph, void, name)
    return 0

# Hook example into the prototype
_zpool_iter_callback_example = ZPOOL_ITER_CALLBACK_PROTOTYPE(__zpool_iter_callback_example)


#
# TODO Pool Create/Destroy
#


## int zpool_create(libzfs_handle_t *, const char *, nvlist_t *,
##                  nvlist_t *, nvlist_t *);
#zpool_create = lz.zpool_create

## int zpool_destroy(zpool_handle_t *);
#zpool_destroy = lz.zpool_destroy

## int zpool_add(zpool_handle_t *, nvlist_t *);
#zpool_add = lz.zpool_add


#extern int zpool_create(libzfs_handle_t *, const char *, nvlist_t *,
#    nvlist_t *, nvlist_t *);
#extern int zpool_destroy(zpool_handle_t *);
#extern int zpool_add(zpool_handle_t *, nvlist_t *);

#typedef struct splitflags {
#    /* do not split, but return the config that would be split off */
#    int dryrun : 1;

#    /* after splitting, import the pool */
#    int import : 1;
#} splitflags_t;


#
# Zfs Iteration
#


# Callback function prototype
# typedef int (*zfs_iter_f)(zfs_handle_t *, void *);
ZFS_ITER_CALLBACK_PROTOTYPE = CFUNCTYPE(c_int, zfs_handle_ptr, c_void_p)


# extern int zfs_iter_root(libzfs_handle_t *, zfs_iter_f, void *);
@C_function(lz)
@annotated(returns=c_int)
def zfs_iter_root(zh=(libzfs_handle_ptr, ),
                  callback=(ZFS_ITER_CALLBACK_PROTOTYPE, None),
                  void=(c_void_p, None),
                  ):
    """ Iterate over all active pools in the system. """
    if callback is None:
        callback = _zfs_iter_callback_example
    return zfs_iter_root.c_function(zh, callback, void)


# extern int zfs_iter_children(zfs_handle_t *, zfs_iter_f, void *);
@C_function(lz)
@annotated(returns=c_int)
def zfs_iter_children(zh=(zfs_handle_ptr, ),
                      callback=(ZFS_ITER_CALLBACK_PROTOTYPE, None),
                      void=(c_void_p, None),
                      ):
    """ Iterate over all active pools in the system. """
    if callback is None:
        callback = _zfs_iter_callback_example
    return zfs_iter_children.c_function(zh, callback, void)


# extern int zfs_iter_dependents(zfs_handle_t *, boolean_t, zfs_iter_f, void *);
@C_function(lz)
@annotated(returns=c_int)
def zfs_iter_dependents(zh=(zfs_handle_ptr, ),
                        boolean=(c_bool, ),
                        callback=(ZFS_ITER_CALLBACK_PROTOTYPE, None),
                        void=(c_void_p, None),
                        ):
    """ Iterate over all active pools in the system. """
    if callback is None:
        callback = _zfs_iter_callback_example
    return zfs_iter_dependents.c_function(zh, boolean, callback, void)


# extern int zfs_iter_filesystems(zfs_handle_t *, zfs_iter_f, void *);
@C_function(lz)
@annotated(returns=c_int)
def zfs_iter_filesystems(zh=(zfs_handle_ptr, ),
                         callback=(ZFS_ITER_CALLBACK_PROTOTYPE, None),
                         void=(c_void_p, None),
                         ):
    """ Iterate over all active pools in the system. """
    if callback is None:
        callback = _zfs_iter_callback_example
    return zfs_iter_filesystems.c_function(zh, callback, void)


# extern int zfs_iter_snapshots(zfs_handle_t *, boolean_t, zfs_iter_f, void *);
@C_function(lz)
@annotated(returns=c_int)
def zfs_iter_snapshots(zh=(zfs_handle_ptr, ),
                       boolean=(c_bool, ),
                       callback=(ZFS_ITER_CALLBACK_PROTOTYPE, None),
                       void=(c_void_p, None),
                       ):
    """ Iterate over all active pools in the system. """
    if callback is None:
        callback = _zfs_iter_callback_example
    return zfs_iter_snapshots.c_function(zh, boolean, callback, void)


# extern int zfs_iter_snapshots_sorted(zfs_handle_t *, zfs_iter_f, void *);
@C_function(lz)
@annotated(returns=c_int)
def zfs_iter_snapshots_sorted(zh=(zfs_handle_ptr, ),
                              callback=(ZFS_ITER_CALLBACK_PROTOTYPE, None),
                              void=(c_void_p, None),
                              ):
    """ Iterate over all active pools in the system. """
    if callback is None:
        callback = _zfs_iter_callback_example
    return zfs_iter_snapshots_sorted.c_function(zh, callback, void)


# extern int zfs_iter_snapspec(zfs_handle_t *, const char *, zfs_iter_f, void *);
@C_function(lz)
@annotated(returns=c_int)
def zfs_iter_snapspec(zh=(zfs_handle_ptr, ),
                      char_p=(c_char_p, ),
                      callback=(ZFS_ITER_CALLBACK_PROTOTYPE, None),
                      void=(c_void_p, None),
                      ):
    """ Iterate over all active pools in the system. """
    if callback is None:
        callback = _zfs_iter_callback_example
    return zfs_iter_snapspec.c_function(zh, char_p, callback, void)


@C_struct()
class get_all_cb_t:
    cb_handles = POINTER(zfs_handle_ptr)
    cb_alloc = c_size_t
    cb_used = c_size_t
    cb_verbose = c_bool


#typedef struct get_all_cb {
#    zfs_handle_t    **cb_handles;
#    c_size_t        cb_alloc;
#    c_size_t        cb_used;
#    boolean_t    cb_verbose;
#    int        (*cb_getone)(zfs_handle_t *, void *);
#} get_all_cb_t;

#void libzfs_add_handle(get_all_cb_t *, zfs_handle_t *);
#int libzfs_dataset_cmp(const void *, const void *);


def __zfs_iter_callback_example(zph, void):
    """ Example zfs_iter callback function that just prints data """
    name = zfs_get_name(zph)
    print "zph=%s void=%s name=%s" % (zph, void, name)
    return 0

# Hook example into the prototype
_zfs_iter_callback_example = ZFS_ITER_CALLBACK_PROTOTYPE(__zfs_iter_callback_example)


#
# TODO Create/Destroy Datasets
#


#extern int zfs_create(libzfs_handle_t *, const char *, zfs_type_t,
#    nvlist_t *);
#extern int zfs_create_ancestors(libzfs_handle_t *, const char *);
#extern int zfs_destroy(zfs_handle_t *, boolean_t);
#extern int zfs_destroy_snaps(zfs_handle_t *, char *, boolean_t);
#extern int zfs_destroy_snaps_nvl(zfs_handle_t *, nvlist_t *, boolean_t);
#extern int zfs_clone(zfs_handle_t *, const char *, nvlist_t *);
#extern int zfs_snapshot(libzfs_handle_t *, const char *, boolean_t, nvlist_t *);
#extern int zfs_rollback(zfs_handle_t *, zfs_handle_t *, boolean_t);
#extern int zfs_rename(zfs_handle_t *, const char *, boolean_t, boolean_t);

#typedef struct sendflags {
#    /* print informational messages (ie, -v was specified) */
#    boolean_t verbose;

#    /* recursive send  (ie, -R) */
#    boolean_t replicate;

#    /* for incrementals, do all intermediate snapshots */
#    boolean_t doall;

#    /* if dataset is a clone, do incremental from its origin */
#    boolean_t fromorigin;

#    /* do deduplication */
#    boolean_t dedup;

#    /* send properties (ie, -p) */
#    boolean_t props;

#    /* do not send (no-op, ie. -n) */
#    boolean_t dryrun;

#    /* parsable verbose output (ie. -P) */
#    boolean_t parsable;

#    /* show progress (ie. -v) */
#    boolean_t progress;
#} sendflags_t;

#typedef boolean_t (snapfilter_cb_t)(zfs_handle_t *, void *);

#extern int zfs_send(zfs_handle_t *, const char *, const char *,
#    sendflags_t *, int, snapfilter_cb_t, void *, nvlist_t **);

#extern int zfs_promote(zfs_handle_t *);
#extern int zfs_hold(zfs_handle_t *, const char *, const char *, boolean_t,
#    boolean_t, boolean_t, int, uint64_t, uint64_t);
#extern int zfs_release(zfs_handle_t *, const char *, const char *, boolean_t);
#extern int zfs_get_holds(zfs_handle_t *, nvlist_t **);
#extern uint64_t zvol_volc_size_to_reservation(uint64_t, nvlist_t *);

#typedef int (*zfs_userspace_cb_t)(void *arg, const char *domain,
#    uid_t rid, uint64_t space);

#extern int zfs_userspace(zfs_handle_t *, zfs_userquota_prop_t,
#    zfs_userspace_cb_t, void *);

#extern int zfs_get_fsacl(zfs_handle_t *, nvlist_t **);
#extern int zfs_set_fsacl(zfs_handle_t *, boolean_t, nvlist_t *);

#typedef struct recvflags {
#    /* print informational messages (ie, -v was specified) */
#    boolean_t verbose;

#    /* the destination is a prefix, not the exact fs (ie, -d) */
#    boolean_t isprefix;

#    /*
#     * Only the tail of the sent snapshot path is appended to the
#     * destination to determine the received snapshot name (ie, -e).
#     */
#    boolean_t istail;

#    /* do not actually do the recv, just check if it would work (ie, -n) */
#    boolean_t dryrun;

#    /* rollback/destroy filesystems as necessary (eg, -F) */
#    boolean_t force;

#    /* set "canmount=off" on all modified filesystems */
#    boolean_t canmountoff;

#    /* byteswap flag is used internally; callers need not specify */
#    boolean_t byteswap;

#    /* do not mount file systems as they are extracted (private) */
#    boolean_t nomount;
#} recvflags_t;

#extern int zfs_receive(libzfs_handle_t *, const char *, recvflags_t *,
#    int, avl_tree_t *);

#typedef enum diff_flags {
#    ZFS_DIFF_PARSEABLE = 0x1,
#    ZFS_DIFF_TIMESTAMP = 0x2,
#    ZFS_DIFF_CLASSIFY = 0x4
#} diff_flags_t;

#extern int zfs_show_diffs(zfs_handle_t *, int, const char *, const char *,
#    int);


#
# TODO Functions to manipulate pool and vdev state
#


# ~trevorj
#extern int zpool_scan(zpool_handle_t *, pool_scan_func_t);
#extern int zpool_clear(zpool_handle_t *, const char *, nvlist_t *);
#extern int zpool_reguid(zpool_handle_t *);
#extern int zpool_reopen(zpool_handle_t *);

#extern int zpool_vdev_online(zpool_handle_t *, const char *, int,
#    vdev_state_t *);
#extern int zpool_vdev_offline(zpool_handle_t *, const char *, boolean_t);
#extern int zpool_vdev_attach(zpool_handle_t *, const char *,
#    const char *, nvlist_t *, int);
#extern int zpool_vdev_detach(zpool_handle_t *, const char *);
#extern int zpool_vdev_remove(zpool_handle_t *, const char *);
#extern int zpool_vdev_split(zpool_handle_t *, char *, nvlist_t **, nvlist_t *,
#    splitflags_t);

#extern int zpool_vdev_fault(zpool_handle_t *, uint64_t, vdev_aux_t);
#extern int zpool_vdev_degrade(zpool_handle_t *, uint64_t, vdev_aux_t);
#extern int zpool_vdev_clear(zpool_handle_t *, uint64_t);

#extern nvlist_t *zpool_find_vdev(zpool_handle_t *, const char *, boolean_t *,
#    boolean_t *, boolean_t *);
#extern nvlist_t *zpool_find_vdev_by_physpath(zpool_handle_t *, const char *,
#    boolean_t *, boolean_t *, boolean_t *);
#extern int zpool_label_disk_wait(char *, int);
#extern int zpool_label_disk(libzfs_handle_t *, zpool_handle_t *, char *);


## int zpool_scan(zpool_handle_t *, pool_scan_func_t);
#zpool_scan = lz.zpool_scan

## int zpool_clear(zpool_handle_t *, const char *, nvlist_t *);
#zpool_clear = lz.zpool_clear

## int zpool_vdev_online(zpool_handle_t *, const char *, int, vdev_state_t *);
#zpool_vdev_online = lz.zpool_vdev_online

## int zpool_vdev_offline(zpool_handle_t *, const char *, boolean_t);
#zpool_vdev_offline = lz.zpool_vdev_offline

## int zpool_vdev_attach(zpool_handle_t *, const char *,
##    const char *, nvlist_t *, int);
#zpool_vdev_attach = lz.zpool_vdev_attach

## int zpool_vdev_detach(zpool_handle_t *, const char *);
#zpool_vdev_detach = lz.zpool_vdev_detach

## int zpool_vdev_remove(zpool_handle_t *, const char *);
#zpool_vdev_remove = lz.zpool_vdev_remove

## int zpool_vdev_split(zpool_handle_t *, char *, nvlist_t **, nvlist_t *,
##    splitflags_t);
#zpool_vdev_split = lz.zpool_vdev_split

## int zpool_vdev_fault(zpool_handle_t *, uint64_t, vdev_aux_t);
#zpool_vdev_fault = lz.zpool_vdev_fault

## int zpool_vdev_degrade(zpool_handle_t *, uint64_t, vdev_aux_t);
#zpool_vdev_degrade = lz.zpool_vdev_degrade

## int zpool_vdev_clear(zpool_handle_t *, uint64_t);
#zpool_vdev_clear = lz.zpool_vdev_clear

## nvlist_t *zpool_find_vdev(zpool_handle_t *, const char *, boolean_t *,
##    boolean_t *, boolean_t *);
#zpool_find_vdev = lz.zpool_find_vdev

## nvlist_t *zpool_find_vdev_by_physpath(zpool_handle_t *, const char *,
##    boolean_t *, boolean_t *, boolean_t *);
#zpool_find_vdev_by_physpath = lz.zpool_find_vdev_by_physpath

## int zpool_label_disk(libzfs_handle_t *, zpool_handle_t *, char *);
#zpool_label_disk = lz.zpool_label_disk


#
# Pool Properties
#


#extern int zpool_set_prop(zpool_handle_t *, const char *, const char *);
zpool_set_prop = _cmeth_bakery(
    lz.zpool_set_prop,
    argtypes=[zpool_handle_ptr, zpool_prop_t, c_char_p],
    restype=c_int,
)


#extern int zpool_get_prop(zpool_handle_t *, zpool_prop_t, char *,
#    c_size_t proplen, zprop_source_t *);
zpool_get_prop = lz.zpool_get_prop
zpool_get_prop.argtypes = [zpool_handle_ptr, zpool_prop_t, c_char_p,
                           c_size_t, zprop_source_t]
zpool_get_prop.restype = c_int

#extern uint64_t zpool_get_prop_int(zpool_handle_t *, zpool_prop_t,
#    zprop_source_t *);
#
#extern const char *zpool_prop_to_name(zpool_prop_t);
#extern const char *zpool_prop_values(zpool_prop_t);


#
# Functions to manage pool properties
#


#extern int zpool_set_prop(zpool_handle_t *, const char *, const char *);
#extern int zpool_get_prop(zpool_handle_t *, zpool_prop_t, char *,
#    c_size_t proplen, zprop_source_t *);
#extern uint64_t zpool_get_prop_int(zpool_handle_t *, zpool_prop_t,
#    zprop_source_t *);

#extern const char *zpool_prop_to_name(zpool_prop_t);
#extern const char *zpool_prop_values(zpool_prop_t);


#
# Pool health statistics.
#


class zpool_status_t(Enumeration):
    _members_ = [
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
    ]


#extern zpool_status_t zpool_get_status(zpool_handle_t *, char **);
#extern zpool_status_t zpool_import_status(nvlist_t *, char **);
#extern void zpool_dump_ddt(const ddt_stat_t *dds, const ddt_histogram_t *ddh);


#
# Statistics and configuration functions.
#


# nvlist_t *zpool_get_config(zpool_handle_t *, nvlist_t **);
_zpool_get_config = _cmeth_bakery(
    lz.zpool_get_config,
    argtypes=[zpool_handle_ptr, nvlist_pp],
    restype=nvlist_p,
)

#extern int zpool_refresh_stats(zpool_handle_t *, boolean_t *);
#extern int zpool_get_errlog(zpool_handle_t *, nvlist_t **);


def zpool_get_config(pool):
    cfg = _zpool_get_config(pool, None)
    return nvlist(cfg)


#
# Import and export functions
#


#extern int zpool_export(zpool_handle_t *, boolean_t);
#extern int zpool_export_force(zpool_handle_t *);
#extern int zpool_import(libzfs_handle_t *, nvlist_t *, const char *,
#    char *altroot);
#extern int zpool_import_props(libzfs_handle_t *, nvlist_t *, const char *,
#    nvlist_t *, int);
#extern void zpool_print_unsup_feat(nvlist_t *config);


if __name__ == "__main__":
    from pprint import pprint as pp
    pp(libzfs_init)
    zh = libzfs_init()
    pp(zh)
    libzfs_fini(zh)
