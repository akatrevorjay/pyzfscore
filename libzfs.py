#!/usr/bin/env python

from _cffi import czfs, czpool, cnvpair, ptop, cdef, ffi
from flufl.enum import IntEnum


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


""" Start """


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


""" Library initialization """

'''
/*
 * Library initialization
 */
extern libzfs_handle_t *libzfs_init(void);
extern void libzfs_fini(libzfs_handle_t *);

extern libzfs_handle_t *zpool_get_handle(zpool_handle_t *);
extern libzfs_handle_t *zfs_get_handle(zfs_handle_t *);

extern void libzfs_print_on_error(libzfs_handle_t *, boolean_t);

extern int libzfs_errno(libzfs_handle_t *);
extern const char *libzfs_error_action(libzfs_handle_t *);
extern const char *libzfs_error_description(libzfs_handle_t *);
extern void libzfs_mnttab_init(libzfs_handle_t *);
extern void libzfs_mnttab_fini(libzfs_handle_t *);
extern void libzfs_mnttab_cache(libzfs_handle_t *, boolean_t);
extern int libzfs_mnttab_find(libzfs_handle_t *, const char *,
    struct mnttab *);
extern void libzfs_mnttab_add(libzfs_handle_t *, const char *,
    const char *, const char *);
extern void libzfs_mnttab_remove(libzfs_handle_t *, const char *);
'''


@cdef('void libzfs_fini(libzfs_handle_t *);')
def libzfs_fini(zhp):
    """Closes libzfs_handle"""
    return czfs.libzfs_fini(zhp)


@cdef('libzfs_handle_t *libzfs_init(void);')
def libzfs_init():
    """Initialize libzfs_handle"""
    return ffi.gc(czfs.libzfs_init(), libzfs_fini)


@cdef('libzfs_handle_t *zpool_get_handle(zpool_handle_t *);')
def zpool_get_handle(zhp):
    """Get libzfs handle from zpool_handle"""
    return czfs.zpool_get_handle(zhp)


@cdef('libzfs_handle_t *zfs_get_handle(zfs_handle_t *);')
def zfs_get_handle(zhp):
    """Get libzfs handle from zfs_handle"""
    return czfs.zpool_get_handle(zhp)


""" Basic handle functions """

'''
/*
 * Basic handle functions
 */
extern zpool_handle_t *zpool_open(libzfs_handle_t *, const char *);
extern zpool_handle_t *zpool_open_canfail(libzfs_handle_t *, const char *);
extern void zpool_close(zpool_handle_t *);
extern const char *zpool_get_name(zpool_handle_t *);
extern int zpool_get_state(zpool_handle_t *);
extern char *zpool_state_to_name(vdev_state_t, vdev_aux_t);
extern const char *zpool_pool_state_to_name(pool_state_t);
extern void zpool_free_handles(libzfs_handle_t *);
'''


@cdef('void zpool_close(zpool_handle_t *);')
def zpool_close(zhp):
    """Close zpool_handle"""
    return czfs.zpool_close(zhp)


@cdef('zpool_handle_t *zpool_open(libzfs_handle_t *, const char *);')
def zpool_open(zhp, name):
    """Open zpool_handle"""
    return ffi.gc(czfs.zpool_open(zhp, name), zpool_close)


@cdef('const char *zpool_get_name(zpool_handle_t *);')
def zpool_get_name(zhp):
    """Get name for zpool_handle"""
    return ffi.string(czfs.zpool_get_name(zhp))


@cdef('int zpool_get_state(zpool_handle_t *);')
def zpool_get_state(zhp):
    """Returns state for zpool_handle"""
    return czfs.zpool_get_state(zhp)


#@cdef('char *zpool_state_to_name(vdev_state_t, vdev_aux_t);')
#def zpool_state_to_name(vdev_state, vdev_aux):
#    return czfs.zpool_state_to_name(vdev_state, vdev_aux)


#@cdef('const char *zpool_pool_state_to_name(pool_state_t);')
#def zpool_pool_state_to_name(pool_state):
#    return czfs.zpool_pool_state_to_name(pool_state)


""" Iterate over all active pools in the system """

'''
/*
 * Iterate over all active pools in the system.
 */
typedef int (*zpool_iter_f)(zpool_handle_t *, void *);
extern int zpool_iter(libzfs_handle_t *, zpool_iter_f, void *);
'''


cdef('typedef int (*zpool_iter_f)(zpool_handle_t *, void *);')


@cdef('int zpool_iter(libzfs_handle_t *, zpool_iter_f, void *);')
def zpool_iter(zhp, handler, arg=None):
    return czfs.zpool_iter(zhp, handler, ffi.new_handle(arg))


'''
/*
 * Functions to create and destroy pools
 */
extern int zpool_create(libzfs_handle_t *, const char *, nvlist_t *,
    nvlist_t *, nvlist_t *);
extern int zpool_destroy(zpool_handle_t *);
extern int zpool_add(zpool_handle_t *, nvlist_t *);

typedef struct splitflags {
	/* do not split, but return the config that would be split off */
	int dryrun : 1;

	/* after splitting, import the pool */
	int import : 1;
} splitflags_t;
'''


""" Functions to manipulate pool and vdev state """

'''
/*
 * Functions to manipulate pool and vdev state
 */
extern int zpool_scan(zpool_handle_t *, pool_scan_func_t);
extern int zpool_clear(zpool_handle_t *, const char *, nvlist_t *);
extern int zpool_reguid(zpool_handle_t *);
extern int zpool_reopen(zpool_handle_t *);

extern int zpool_vdev_online(zpool_handle_t *, const char *, int,
    vdev_state_t *);
extern int zpool_vdev_offline(zpool_handle_t *, const char *, boolean_t);
extern int zpool_vdev_attach(zpool_handle_t *, const char *,
    const char *, nvlist_t *, int);
extern int zpool_vdev_detach(zpool_handle_t *, const char *);
extern int zpool_vdev_remove(zpool_handle_t *, const char *);
extern int zpool_vdev_split(zpool_handle_t *, char *, nvlist_t **, nvlist_t *,
    splitflags_t);

extern int zpool_vdev_fault(zpool_handle_t *, uint64_t, vdev_aux_t);
extern int zpool_vdev_degrade(zpool_handle_t *, uint64_t, vdev_aux_t);
extern int zpool_vdev_clear(zpool_handle_t *, uint64_t);

extern nvlist_t *zpool_find_vdev(zpool_handle_t *, const char *, boolean_t *,
    boolean_t *, boolean_t *);
extern nvlist_t *zpool_find_vdev_by_physpath(zpool_handle_t *, const char *,
    boolean_t *, boolean_t *, boolean_t *);
extern int zpool_label_disk_wait(char *, int);
extern int zpool_label_disk(libzfs_handle_t *, zpool_handle_t *, char *);
'''

#@cdef('int zpool_clear(zpool_handle_t *, const char *, nvlist_t *);')
#def zpool_clear(zhp, blah, nvblah):
#    pass


'''
/*
 * Functions to manage pool properties
 */
extern int zpool_set_prop(zpool_handle_t *, const char *, const char *);
extern int zpool_get_prop(zpool_handle_t *, zpool_prop_t, char *,
    size_t proplen, zprop_source_t *);
extern uint64_t zpool_get_prop_int(zpool_handle_t *, zpool_prop_t,
    zprop_source_t *);

extern const char *zpool_prop_to_name(zpool_prop_t);
extern const char *zpool_prop_values(zpool_prop_t);
'''


""" Pool health statistics """

cdef('typedef enum { ...} zpool_status_t;')

'''
extern zpool_status_t zpool_get_status(zpool_handle_t *, char **);
extern zpool_status_t zpool_import_status(nvlist_t *, char **);
extern void zpool_dump_ddt(const ddt_stat_t *dds, const ddt_histogram_t *ddh);
'''

@cdef('zpool_status_t zpool_get_status(zpool_handle_t *, char **);')
def zpool_get_status(zhp, arg=None):
    """Get status of zpool"""
    return czfs.zpool_get_status(zhp, arg)


'''
/*
 * Statistics and configuration functions.
 */
extern nvlist_t *zpool_get_config(zpool_handle_t *, nvlist_t **);
extern nvlist_t *zpool_get_features(zpool_handle_t *);
extern int zpool_refresh_stats(zpool_handle_t *, boolean_t *);
extern int zpool_get_errlog(zpool_handle_t *, nvlist_t **);
'''

'''
/*
 * Import and export functions
 */
extern int zpool_export(zpool_handle_t *, boolean_t);
extern int zpool_export_force(zpool_handle_t *);
extern int zpool_import(libzfs_handle_t *, nvlist_t *, const char *,
    char *altroot);
extern int zpool_import_props(libzfs_handle_t *, nvlist_t *, const char *,
    nvlist_t *, int);
extern void zpool_print_unsup_feat(nvlist_t *config);
'''

'''
/*
 * Search for pools to import
 */

typedef struct importargs {
	char **path;		/* a list of paths to search		*/
	int paths;		/* number of paths to search		*/
	char *poolname;		/* name of a pool to find		*/
	uint64_t guid;		/* guid of a pool to find		*/
	char *cachefile;	/* cachefile to use for import		*/
	int can_be_active : 1;	/* can the pool be active?		*/
	int unique : 1;		/* does 'poolname' already exist?	*/
	int exists : 1;		/* set on return if pool already exists	*/
} importargs_t;

extern nvlist_t *zpool_search_import(libzfs_handle_t *, importargs_t *);

/* legacy pool search routines */
extern nvlist_t *zpool_find_import(libzfs_handle_t *, int, char **);
extern nvlist_t *zpool_find_import_cached(libzfs_handle_t *, const char *,
    char *, uint64_t);
'''

'''
/*
 * Miscellaneous pool functions
 */
struct zfs_cmd;

extern const char *zfs_history_event_names[LOG_END];

extern char *zpool_vdev_name(libzfs_handle_t *, zpool_handle_t *, nvlist_t *,
    boolean_t verbose);
extern int zpool_upgrade(zpool_handle_t *, uint64_t);
extern int zpool_get_history(zpool_handle_t *, nvlist_t **);
extern int zpool_history_unpack(char *, uint64_t, uint64_t *,
    nvlist_t ***, uint_t *);
extern void zpool_set_history_str(const char *subcommand, int argc,
    char **argv, char *history_str);
extern int zpool_stage_history(libzfs_handle_t *, const char *);
extern int zpool_events_next(libzfs_handle_t *, nvlist_t **, int *, int, int);
extern int zpool_events_clear(libzfs_handle_t *, int *);
extern void zpool_obj_to_path(zpool_handle_t *, uint64_t, uint64_t, char *,
    size_t len);
extern int zfs_ioctl(libzfs_handle_t *, int, struct zfs_cmd *);
extern int zpool_get_physpath(zpool_handle_t *, char *, size_t);
extern void zpool_explain_recover(libzfs_handle_t *, const char *, int,
    nvlist_t *);
'''


""" Basic handle manipulation """

'''
/*
 * Basic handle manipulations.  These functions do not create or destroy the
 * underlying datasets, only the references to them.
 */
extern zfs_handle_t *zfs_open(libzfs_handle_t *, const char *, int);
extern zfs_handle_t *zfs_handle_dup(zfs_handle_t *);
extern void zfs_close(zfs_handle_t *);
extern zfs_type_t zfs_get_type(const zfs_handle_t *);
extern const char *zfs_get_name(const zfs_handle_t *);
extern zpool_handle_t *zfs_get_pool_handle(const zfs_handle_t *);
'''


@cdef('void zfs_close(zfs_handle_t *);')
def zfs_close(zhp):
    """Closes zfs_handle"""
    return czfs.zfs_close(zhp)


@cdef('zfs_handle_t *zfs_open(libzfs_handle_t *, const char *, int);')
def zfs_open(zhp, name, types_mask=sum(zfs_type_t)):
    """Gets zfs_handle for dataset"""
    return ffi.gc(czfs.zfs_open(zhp, name, types_mask), zfs_close)


@cdef('int zfs_get_type(const zfs_handle_t *);')
def zfs_get_type(zhp):
    """Gets type for zfs_handle"""
    return zfs_type_t[czfs.zfs_get_type(zhp)]


@cdef('const char *zfs_get_name(const zfs_handle_t *);')
def zfs_get_name(zhp):
    """Gets name for zfs_handle"""
    return ffi.string(czfs.zfs_get_name(zhp))


@cdef('zpool_handle_t *zfs_get_pool_handle(const zfs_handle_t *);')
def zfs_get_pool_handle(zhp):
    """Gets pool handle for zfs_handle"""
    return czfs.zfs_get_pool_handle(zhp)


'''
/*
 * Property management functions.  Some functions are shared with the kernel,
 * and are found in sys/fs/zfs.h.
 */

/*
 * zfs dataset property management
 */
extern const char *zfs_prop_default_string(zfs_prop_t);
extern uint64_t zfs_prop_default_numeric(zfs_prop_t);
extern const char *zfs_prop_column_name(zfs_prop_t);
extern boolean_t zfs_prop_align_right(zfs_prop_t);

extern nvlist_t *zfs_valid_proplist(libzfs_handle_t *, zfs_type_t,
    nvlist_t *, uint64_t, zfs_handle_t *, const char *);

extern const char *zfs_prop_to_name(zfs_prop_t);
extern int zfs_prop_set(zfs_handle_t *, const char *, const char *);
extern int zfs_prop_get(zfs_handle_t *, zfs_prop_t, char *, size_t,
    zprop_source_t *, char *, size_t, boolean_t);
extern int zfs_prop_get_recvd(zfs_handle_t *, const char *, char *, size_t,
    boolean_t);
extern int zfs_prop_get_numeric(zfs_handle_t *, zfs_prop_t, uint64_t *,
    zprop_source_t *, char *, size_t);
extern int zfs_prop_get_userquota_int(zfs_handle_t *zhp, const char *propname,
    uint64_t *propvalue);
extern int zfs_prop_get_userquota(zfs_handle_t *zhp, const char *propname,
    char *propbuf, int proplen, boolean_t literal);
extern int zfs_prop_get_written_int(zfs_handle_t *zhp, const char *propname,
    uint64_t *propvalue);
extern int zfs_prop_get_written(zfs_handle_t *zhp, const char *propname,
    char *propbuf, int proplen, boolean_t literal);
extern int zfs_prop_get_feature(zfs_handle_t *zhp, const char *propname,
    char *buf, size_t len);
extern int zfs_get_snapused_int(zfs_handle_t *firstsnap, zfs_handle_t *lastsnap,
    uint64_t *usedp);
extern uint64_t getprop_uint64(zfs_handle_t *, zfs_prop_t, char **);
extern uint64_t zfs_prop_get_int(zfs_handle_t *, zfs_prop_t);
extern int zfs_prop_inherit(zfs_handle_t *, const char *, boolean_t);
extern const char *zfs_prop_values(zfs_prop_t);
extern int zfs_prop_is_string(zfs_prop_t prop);
extern nvlist_t *zfs_get_user_props(zfs_handle_t *);
extern nvlist_t *zfs_get_recvd_props(zfs_handle_t *);
extern nvlist_t *zfs_get_clones_nvl(zfs_handle_t *);

typedef struct zprop_list {
	int		pl_prop;
	char		*pl_user_prop;
	struct zprop_list *pl_next;
	boolean_t	pl_all;
	size_t		pl_width;
	size_t		pl_recvd_width;
	boolean_t	pl_fixed;
} zprop_list_t;

extern int zfs_expand_proplist(zfs_handle_t *, zprop_list_t **, boolean_t);
extern void zfs_prune_proplist(zfs_handle_t *, uint8_t *);
'''



'''
/*
 * zpool property management
 */
extern int zpool_expand_proplist(zpool_handle_t *, zprop_list_t **);
extern int zpool_prop_get_feature(zpool_handle_t *, const char *, char *,
    size_t);
extern const char *zpool_prop_default_string(zpool_prop_t);
extern uint64_t zpool_prop_default_numeric(zpool_prop_t);
extern const char *zpool_prop_column_name(zpool_prop_t);
extern boolean_t zpool_prop_align_right(zpool_prop_t);
'''

'''
/*
 * Functions shared by zfs and zpool property management.
 */
extern int zprop_iter(zprop_func func, void *cb, boolean_t show_all,
    boolean_t ordered, zfs_type_t type);
extern int zprop_get_list(libzfs_handle_t *, char *, zprop_list_t **,
    zfs_type_t);
extern void zprop_free_list(zprop_list_t *);

#define	ZFS_GET_NCOLS	5

typedef enum {
	GET_COL_NONE,
	GET_COL_NAME,
	GET_COL_PROPERTY,
	GET_COL_VALUE,
	GET_COL_RECVD,
	GET_COL_SOURCE
} zfs_get_column_t;

/*
 * Functions for printing zfs or zpool properties
 */
typedef struct zprop_get_cbdata {
	int cb_sources;
	zfs_get_column_t cb_columns[ZFS_GET_NCOLS];
	int cb_colwidths[ZFS_GET_NCOLS + 1];
	boolean_t cb_scripted;
	boolean_t cb_literal;
	boolean_t cb_first;
	zprop_list_t *cb_proplist;
	zfs_type_t cb_type;
} zprop_get_cbdata_t;

void zprop_print_one_property(const char *, zprop_get_cbdata_t *,
    const char *, const char *, zprop_source_t, const char *,
    const char *);
'''

""" Iterator functions """

'''
/*
 * Iterator functions.
 */
typedef int (*zfs_iter_f)(zfs_handle_t *, void *);
extern int zfs_iter_root(libzfs_handle_t *, zfs_iter_f, void *);
extern int zfs_iter_children(zfs_handle_t *, zfs_iter_f, void *);
extern int zfs_iter_dependents(zfs_handle_t *, boolean_t, zfs_iter_f, void *);
extern int zfs_iter_filesystems(zfs_handle_t *, zfs_iter_f, void *);
extern int zfs_iter_snapshots(zfs_handle_t *, boolean_t, zfs_iter_f, void *);
extern int zfs_iter_snapshots_sorted(zfs_handle_t *, zfs_iter_f, void *);
extern int zfs_iter_snapspec(zfs_handle_t *, const char *, zfs_iter_f, void *);

typedef struct get_all_cb {
	zfs_handle_t	**cb_handles;
	size_t		cb_alloc;
	size_t		cb_used;
	boolean_t	cb_verbose;
	int		(*cb_getone)(zfs_handle_t *, void *);
} get_all_cb_t;

void libzfs_add_handle(get_all_cb_t *, zfs_handle_t *);
int libzfs_dataset_cmp(const void *, const void *);
'''

cdef('typedef int (*zfs_iter_f)(zfs_handle_t *, void *);')

@cdef('int zfs_iter_root(libzfs_handle_t *, zfs_iter_f, void *);')
def zfs_iter_root(zhp, handler, arg=None):
    return czfs.zfs_iter_root(zhp, handler, ffi.new_handle(arg))

@cdef('int zfs_iter_children(zfs_handle_t *, zfs_iter_f, void *);')
def zfs_iter_children(zhp, handler, arg=None):
    return czfs.zfs_iter_children(zhp, handler, ffi.new_handle(arg))

## TODO what is boolean_t for? Name accordingly.
#@cdef('int zfs_iter_dependents(zfs_handle_t *, boolean_t, zfs_iter_f, void *);')
#def zfs_iter_dependents(zhp, b, handler, arg=None):
#    return czfs.zfs_iter_dependents(zhp, b, handler, ffi.new_handle(arg))

@cdef('int zfs_iter_filesystems(zfs_handle_t *, zfs_iter_f, void *);')
def zfs_iter_filesystems(zhp, handler, arg=None):
    return czfs.zfs_iter_filesystems(zhp, handler, ffi.new_handle(arg))

## TODO what is boolean_t for? Name accordingly.
#@cdef('int zfs_iter_snapshots(zfs_handle_t *, boolean_t, zfs_iter_f, void *);')
#def zfs_iter_snapshots(zhp, b, handler, arg=None):
#    return czfs.zfs_iter_snapshots(zhp, b, handler, ffi.new_handle(arg))

@cdef('int zfs_iter_snapshots_sorted(zfs_handle_t *, zfs_iter_f, void *);')
def zfs_iter_snapshots_sorted(zhp, handler, arg=None):
    return czfs.zfs_iter_snapshots_sorted(zhp, handler, ffi.new_handle(arg))

# TODO what is const char * for? Name accordingly.
@cdef('int zfs_iter_snapspec(zfs_handle_t *, const char *, zfs_iter_f, void *);')
def zfs_iter_snapspec(zhp, c, handler, arg=None):
    return czfs.zfs_iter_snapspec(zhp, c, handler, ffi.new_handle(arg))


'''
/*
 * Functions to create and destroy datasets.
 */
extern int zfs_create(libzfs_handle_t *, const char *, zfs_type_t,
    nvlist_t *);
extern int zfs_create_ancestors(libzfs_handle_t *, const char *);
extern int zfs_destroy(zfs_handle_t *, boolean_t);
extern int zfs_destroy_snaps(zfs_handle_t *, char *, boolean_t);
extern int zfs_destroy_snaps_nvl(zfs_handle_t *, nvlist_t *, boolean_t);
extern int zfs_clone(zfs_handle_t *, const char *, nvlist_t *);
extern int zfs_snapshot(libzfs_handle_t *, const char *, boolean_t, nvlist_t *);
extern int zfs_rollback(zfs_handle_t *, zfs_handle_t *, boolean_t);
extern int zfs_rename(zfs_handle_t *, const char *, boolean_t, boolean_t);

typedef struct sendflags {
	/* print informational messages (ie, -v was specified) */
	boolean_t verbose;

	/* recursive send  (ie, -R) */
	boolean_t replicate;

	/* for incrementals, do all intermediate snapshots */
	boolean_t doall;

	/* if dataset is a clone, do incremental from its origin */
	boolean_t fromorigin;

	/* do deduplication */
	boolean_t dedup;

	/* send properties (ie, -p) */
	boolean_t props;

	/* do not send (no-op, ie. -n) */
	boolean_t dryrun;

	/* parsable verbose output (ie. -P) */
	boolean_t parsable;

	/* show progress (ie. -v) */
	boolean_t progress;
} sendflags_t;

typedef boolean_t (snapfilter_cb_t)(zfs_handle_t *, void *);

extern int zfs_send(zfs_handle_t *, const char *, const char *,
    sendflags_t *, int, snapfilter_cb_t, void *, nvlist_t **);

extern int zfs_promote(zfs_handle_t *);
extern int zfs_hold(zfs_handle_t *, const char *, const char *, boolean_t,
    boolean_t, boolean_t, int, uint64_t, uint64_t);
extern int zfs_release(zfs_handle_t *, const char *, const char *, boolean_t);
extern int zfs_get_holds(zfs_handle_t *, nvlist_t **);
extern uint64_t zvol_volsize_to_reservation(uint64_t, nvlist_t *);

typedef int (*zfs_userspace_cb_t)(void *arg, const char *domain,
    uid_t rid, uint64_t space);

extern int zfs_userspace(zfs_handle_t *, zfs_userquota_prop_t,
    zfs_userspace_cb_t, void *);

extern int zfs_get_fsacl(zfs_handle_t *, nvlist_t **);
extern int zfs_set_fsacl(zfs_handle_t *, boolean_t, nvlist_t *);

typedef struct recvflags {
	/* print informational messages (ie, -v was specified) */
	boolean_t verbose;

	/* the destination is a prefix, not the exact fs (ie, -d) */
	boolean_t isprefix;

	/*
	 * Only the tail of the sent snapshot path is appended to the
	 * destination to determine the received snapshot name (ie, -e).
	 */
	boolean_t istail;

	/* do not actually do the recv, just check if it would work (ie, -n) */
	boolean_t dryrun;

	/* rollback/destroy filesystems as necessary (eg, -F) */
	boolean_t force;

	/* set "canmount=off" on all modified filesystems */
	boolean_t canmountoff;

	/* byteswap flag is used internally; callers need not specify */
	boolean_t byteswap;

	/* do not mount file systems as they are extracted (private) */
	boolean_t nomount;
} recvflags_t;

extern int zfs_receive(libzfs_handle_t *, const char *, recvflags_t *,
    int, avl_tree_t *);

typedef enum diff_flags {
	ZFS_DIFF_PARSEABLE = 0x1,
	ZFS_DIFF_TIMESTAMP = 0x2,
	ZFS_DIFF_CLASSIFY = 0x4
} diff_flags_t;

extern int zfs_show_diffs(zfs_handle_t *, int, const char *, const char *,
    int);
'''

'''
/*
 * Miscellaneous functions.
 */
extern const char *zfs_type_to_name(zfs_type_t);
extern void zfs_refresh_properties(zfs_handle_t *);
extern int zfs_name_valid(const char *, zfs_type_t);
extern zfs_handle_t *zfs_path_to_zhandle(libzfs_handle_t *, char *, zfs_type_t);
extern boolean_t zfs_dataset_exists(libzfs_handle_t *, const char *,
    zfs_type_t);
extern int zfs_spa_version(zfs_handle_t *, int *);
extern int zfs_append_partition(char *path, size_t max_len);
extern int zfs_resolve_shortname(const char *name, char *path, size_t pathlen);
extern int zfs_strcmp_pathname(char *name, char *cmp_name, int wholedisk);
'''

'''
/*
 * Mount support functions.
 */
extern boolean_t is_mounted(libzfs_handle_t *, const char *special, char **);
extern boolean_t zfs_is_mounted(zfs_handle_t *, char **);
extern int zfs_mount(zfs_handle_t *, const char *, int);
extern int zfs_unmount(zfs_handle_t *, const char *, int);
extern int zfs_unmountall(zfs_handle_t *, int);
'''

'''
/*
 * Share support functions.
 */
extern boolean_t zfs_is_shared(zfs_handle_t *);
extern int zfs_share(zfs_handle_t *);
extern int zfs_unshare(zfs_handle_t *);
'''

'''
/*
 * Protocol-specific share support functions.
 */
extern boolean_t zfs_is_shared_nfs(zfs_handle_t *, char **);
extern boolean_t zfs_is_shared_smb(zfs_handle_t *, char **);
extern int zfs_share_nfs(zfs_handle_t *);
extern int zfs_share_smb(zfs_handle_t *);
extern int zfs_shareall(zfs_handle_t *);
extern int zfs_unshare_nfs(zfs_handle_t *, const char *);
extern int zfs_unshare_smb(zfs_handle_t *, const char *);
extern int zfs_unshareall_nfs(zfs_handle_t *);
extern int zfs_unshareall_smb(zfs_handle_t *);
extern int zfs_unshareall_bypath(zfs_handle_t *, const char *);
extern int zfs_unshareall(zfs_handle_t *);
extern int zfs_deleg_share_nfs(libzfs_handle_t *, char *, char *, char *,
    void *, void *, int, zfs_share_op_t);
'''

'''
/*
 * Utility function to convert a number to a human-readable form.
 */
extern void zfs_nicenum(uint64_t, char *, size_t);
extern int zfs_nicestrtonum(libzfs_handle_t *, const char *, uint64_t *);
'''

'''
/*
 * Utility functions to run an external process.
 */
#define	STDOUT_VERBOSE	0x01
#define	STDERR_VERBOSE	0x02

int libzfs_run_process(const char *, char **, int flags);
int libzfs_load_module(const char *);

/*
 * Given a device or file, determine if it is part of a pool.
 */
extern int zpool_in_use(libzfs_handle_t *, int, pool_state_t *, char **,
    boolean_t *);

/*
 * Label manipulation.
 */
extern int zpool_read_label(int, nvlist_t **);
extern int zpool_clear_label(int);

/*
 * Management interfaces for SMB ACL files
 */

int zfs_smb_acl_add(libzfs_handle_t *, char *, char *, char *);
int zfs_smb_acl_remove(libzfs_handle_t *, char *, char *, char *);
int zfs_smb_acl_purge(libzfs_handle_t *, char *, char *);
int zfs_smb_acl_rename(libzfs_handle_t *, char *, char *, char *, char *);

/*
 * Enable and disable datasets within a pool by mounting/unmounting and
 * sharing/unsharing them.
 */
extern int zpool_enable_datasets(zpool_handle_t *, const char *, int);
extern int zpool_disable_datasets(zpool_handle_t *, boolean_t);

/*
 * Mappings between vdev and FRU.
 */
extern void libzfs_fru_refresh(libzfs_handle_t *);
extern const char *libzfs_fru_lookup(libzfs_handle_t *, const char *);
extern const char *libzfs_fru_devpath(libzfs_handle_t *, const char *);
extern boolean_t libzfs_fru_compare(libzfs_handle_t *, const char *,
    const char *);
extern boolean_t libzfs_fru_notself(libzfs_handle_t *, const char *);
extern int zpool_fru_set(zpool_handle_t *, uint64_t, const char *);
'''


ffi.verify('''
#include <libzfs.h>
#include <sys/fs/zfs.h>
''',
    define_macros=[
        ('NDEBUG', 1),
        ('HAVE_IOCTL_IN_SYS_IOCTL_H', 1)
    ],
    include_dirs=['/usr/include/libzfs', '/usr/include/libspl'],
    libraries=['nvpair', 'zfs', 'zpool'],
)



