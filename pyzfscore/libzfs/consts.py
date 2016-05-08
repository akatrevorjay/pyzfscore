from ..flufl.enum import IntEnum

from ._cffi import ffi


libzfs_errors = IntEnum(
    'libzfs_errors', [
        'EZFS_NOMEM',  # out of memory
        'EZFS_BADPROP',  # invalid property value
        'EZFS_PROPREADONLY',  # cannot set readonly property
        'EZFS_PROPTYPE',  # property does not apply to dataset type
        'EZFS_PROPNONINHERIT',  # property is not inheritable
        'EZFS_PROPSPACE',  # bad quota or reservation
        'EZFS_BADTYPE',  # dataset is not of appropriate type
        'EZFS_BUSY',  # pool or dataset is busy
        'EZFS_EXISTS',  # pool or dataset already exists
        'EZFS_NOENT',  # no such pool or dataset
        'EZFS_BADSTREAM',  # bad backup stream
        'EZFS_DSREADONLY',  # dataset is readonly
        'EZFS_VOLTOOBIG',  # volume is too large for 32-bit system
        'EZFS_INVALIDNAME',  # invalid dataset name
        'EZFS_BADRESTORE',  # unable to restore to destination
        'EZFS_BADBACKUP',  # backup failed
        'EZFS_BADTARGET',  # bad attach/detach/replace target
        'EZFS_NODEVICE',  # no such device in pool
        'EZFS_BADDEV',  # invalid device to add
        'EZFS_NOREPLICAS',  # no valid replicas
        'EZFS_RESILVERING',  # currently resilvering
        'EZFS_BADVERSION',  # unsupported version
        'EZFS_POOLUNAVAIL',  # pool is currently unavailable
        'EZFS_DEVOVERFLOW',  # too many devices in one vdev
        'EZFS_BADPATH',  # must be an absolute path
        'EZFS_CROSSTARGET',  # rename or clone across pool or dataset
        'EZFS_ZONED',  # used improperly in local zone
        'EZFS_MOUNTFAILED',  # failed to mount dataset
        'EZFS_UMOUNTFAILED',  # failed to unmount dataset
        'EZFS_UNSHARENFSFAILED',  # unshare(1M) failed
        'EZFS_SHARENFSFAILED',  # share(1M) failed
        'EZFS_PERM',  # permission denied
        'EZFS_NOSPC',  # out of space
        'EZFS_FAULT',  # bad address
        'EZFS_IO',  # I/O error
        'EZFS_INTR',  # signal received
        'EZFS_ISSPARE',  # device is a hot spare
        'EZFS_INVALCONFIG',  # invalid vdev configuration
        'EZFS_RECURSIVE',  # recursive dependency
        'EZFS_NOHISTORY',  # no history object
        'EZFS_POOLPROPS',  # couldn't retrieve pool props
        'EZFS_POOL_NOTSUP',  # ops not supported for this type of pool
        'EZFS_POOL_INVALARG',  # invalid argument for this pool operation
        'EZFS_NAMETOOLONG',  # dataset name is too long
        'EZFS_OPENFAILED',  # open of device failed
        'EZFS_NOCAP',  # couldn't get capacity
        'EZFS_LABELFAILED',  # write of label failed
        'EZFS_BADWHO',  # invalid permission who
        'EZFS_BADPERM',  # invalid permission
        'EZFS_BADPERMSET',  # invalid permission set name
        'EZFS_NODELEGATION',  # delegated administration is disabled
        'EZFS_UNSHARESMBFAILED',  # failed to unshare over smb
        'EZFS_SHARESMBFAILED',  # failed to share over smb
        'EZFS_BADCACHE',  # bad cache file
        'EZFS_ISL2CACHE',  # device is for the level 2 ARC
        'EZFS_VDEVNOTSUP',  # unsupported vdev type
        'EZFS_NOTSUP',  # ops not supported on this dataset
        'EZFS_ACTIVE_SPARE',  # pool has active shared spare devices
        'EZFS_UNPLAYED_LOGS',  # log device has unplayed logs
        'EZFS_REFTAG_RELE',  # snapshot release: tag not found
        'EZFS_REFTAG_HOLD',  # snapshot hold: tag already exists
        'EZFS_TAGTOOLONG',  # snapshot hold/rele: tag too long
        'EZFS_PIPEFAILED',  # pipe create failed
        'EZFS_THREADCREATEFAILED',  # thread create failed
        'EZFS_POSTSPLIT_ONLINE',  # onlining a disk after splitting it
        'EZFS_SCRUBBING',  # currently scrubbing
        'EZFS_NO_SCRUB',  # no active scrub
        'EZFS_DIFF',  # general failure of zfs diff
        'EZFS_DIFFDATA',  # bad zfs diff data
        'EZFS_POOLREADONLY',  # pool is in read-only mode
        'EZFS_UNKNOWN'
    ], start=2000)

ffi.cdef('''
/*
 * libzfs errors
 */
typedef enum {
    EZFS_NOMEM = 2000,	/* out of memory */
    EZFS_BADPROP,		/* invalid property value */
    EZFS_PROPREADONLY,	/* cannot set readonly property */
    EZFS_PROPTYPE,		/* property does not apply to dataset type */
    EZFS_PROPNONINHERIT,	/* property is not inheritable */
    EZFS_PROPSPACE,		/* bad quota or reservation */
    EZFS_BADTYPE,		/* dataset is not of appropriate type */
    EZFS_BUSY,		/* pool or dataset is busy */
    EZFS_EXISTS,		/* pool or dataset already exists */
    EZFS_NOENT,		/* no such pool or dataset */
    EZFS_BADSTREAM,		/* bad backup stream */
    EZFS_DSREADONLY,	/* dataset is readonly */
    EZFS_VOLTOOBIG,		/* volume is too large for 32-bit system */
    EZFS_INVALIDNAME,	/* invalid dataset name */
    EZFS_BADRESTORE,	/* unable to restore to destination */
    EZFS_BADBACKUP,		/* backup failed */
    EZFS_BADTARGET,		/* bad attach/detach/replace target */
    EZFS_NODEVICE,		/* no such device in pool */
    EZFS_BADDEV,		/* invalid device to add */
    EZFS_NOREPLICAS,	/* no valid replicas */
    EZFS_RESILVERING,	/* currently resilvering */
    EZFS_BADVERSION,	/* unsupported version */
    EZFS_POOLUNAVAIL,	/* pool is currently unavailable */
    EZFS_DEVOVERFLOW,	/* too many devices in one vdev */
    EZFS_BADPATH,		/* must be an absolute path */
    EZFS_CROSSTARGET,	/* rename or clone across pool or dataset */
    EZFS_ZONED,		/* used improperly in local zone */
    EZFS_MOUNTFAILED,	/* failed to mount dataset */
    EZFS_UMOUNTFAILED,	/* failed to unmount dataset */
    EZFS_UNSHARENFSFAILED,	/* unshare(1M) failed */
    EZFS_SHARENFSFAILED,	/* share(1M) failed */
    EZFS_PERM,		/* permission denied */
    EZFS_NOSPC,		/* out of space */
    EZFS_FAULT,		/* bad address */
    EZFS_IO,		/* I/O error */
    EZFS_INTR,		/* signal received */
    EZFS_ISSPARE,		/* device is a hot spare */
    EZFS_INVALCONFIG,	/* invalid vdev configuration */
    EZFS_RECURSIVE,		/* recursive dependency */
    EZFS_NOHISTORY,		/* no history object */
    EZFS_POOLPROPS,		/* couldn't retrieve pool props */
    EZFS_POOL_NOTSUP,	/* ops not supported for this type of pool */
    EZFS_POOL_INVALARG,	/* invalid argument for this pool operation */
    EZFS_NAMETOOLONG,	/* dataset name is too long */
    EZFS_OPENFAILED,	/* open of device failed */
    EZFS_NOCAP,		/* couldn't get capacity */
    EZFS_LABELFAILED,	/* write of label failed */
    EZFS_BADWHO,		/* invalid permission who */
    EZFS_BADPERM,		/* invalid permission */
    EZFS_BADPERMSET,	/* invalid permission set name */
    EZFS_NODELEGATION,	/* delegated administration is disabled */
    EZFS_UNSHARESMBFAILED,	/* failed to unshare over smb */
    EZFS_SHARESMBFAILED,	/* failed to share over smb */
    EZFS_BADCACHE,		/* bad cache file */
    EZFS_ISL2CACHE,		/* device is for the level 2 ARC */
    EZFS_VDEVNOTSUP,	/* unsupported vdev type */
    EZFS_NOTSUP,		/* ops not supported on this dataset */
    EZFS_ACTIVE_SPARE,	/* pool has active shared spare devices */
    EZFS_UNPLAYED_LOGS,	/* log device has unplayed logs */
    EZFS_REFTAG_RELE,	/* snapshot release: tag not found */
    EZFS_REFTAG_HOLD,	/* snapshot hold: tag already exists */
    EZFS_TAGTOOLONG,	/* snapshot hold/rele: tag too long */
    EZFS_PIPEFAILED,	/* pipe create failed */
    EZFS_THREADCREATEFAILED, /* thread create failed */
    EZFS_POSTSPLIT_ONLINE,	/* onlining a disk after splitting it */
    EZFS_SCRUBBING,		/* currently scrubbing */
    EZFS_NO_SCRUB,		/* no active scrub */
    EZFS_DIFF,		/* general failure of zfs diff */
    EZFS_DIFFDATA,		/* bad zfs diff data */
    EZFS_POOLREADONLY,	/* pool is in read-only mode */
    EZFS_UNKNOWN
} libzfs_errors_t;
''')

zfs_prop_t = IntEnum('zfs_prop_t', [
    'ZFS_PROP_TYPE',
    'ZFS_PROP_CREATION',
    'ZFS_PROP_USED',
    'ZFS_PROP_AVAILABLE',
    'ZFS_PROP_REFERENCED',
    'ZFS_PROP_COMPRESSRATIO',
    'ZFS_PROP_MOUNTED',
    'ZFS_PROP_ORIGIN',
    'ZFS_PROP_QUOTA',
    'ZFS_PROP_RESERVATION',
    'ZFS_PROP_VOLSIZE',
    'ZFS_PROP_VOLBLOCKSIZE',
    'ZFS_PROP_RECORDSIZE',
    'ZFS_PROP_MOUNTPOINT',
    'ZFS_PROP_SHARENFS',
    'ZFS_PROP_CHECKSUM',
    'ZFS_PROP_COMPRESSION',
    'ZFS_PROP_ATIME',
    'ZFS_PROP_DEVICES',
    'ZFS_PROP_EXEC',
    'ZFS_PROP_SETUID',
    'ZFS_PROP_READONLY',
    'ZFS_PROP_ZONED',
    'ZFS_PROP_SNAPDIR',
    'ZFS_PROP_PRIVATE',
    'ZFS_PROP_ACLINHERIT',
    'ZFS_PROP_CREATETXG',
    'ZFS_PROP_NAME',
    'ZFS_PROP_CANMOUNT',
    'ZFS_PROP_ISCSIOPTIONS',
    'ZFS_PROP_XATTR',
    'ZFS_PROP_NUMCLONES',
    'ZFS_PROP_COPIES',
    'ZFS_PROP_VERSION',
    'ZFS_PROP_UTF8ONLY',
    'ZFS_PROP_NORMALIZE',
    'ZFS_PROP_CASE',
    'ZFS_PROP_VSCAN',
    'ZFS_PROP_NBMAND',
    'ZFS_PROP_SHARESMB',
    'ZFS_PROP_REFQUOTA',
    'ZFS_PROP_REFRESERVATION',
    'ZFS_PROP_GUID',
    'ZFS_PROP_PRIMARYCACHE',
    'ZFS_PROP_SECONDARYCACHE',
    'ZFS_PROP_USEDSNAP',
    'ZFS_PROP_USEDDS',
    'ZFS_PROP_USEDCHILD',
    'ZFS_PROP_USEDREFRESERV',
    'ZFS_PROP_USERACCOUNTING',
    'ZFS_PROP_STMF_SHAREINFO',
    'ZFS_PROP_DEFER_DESTROY',
    'ZFS_PROP_USERREFS',
    'ZFS_PROP_LOGBIAS',
    'ZFS_PROP_UNIQUE',
    'ZFS_PROP_OBJSETID',
    'ZFS_PROP_DEDUP',
    'ZFS_PROP_MLSLABEL',
    'ZFS_PROP_SYNC',
    'ZFS_PROP_REFRATIO',
    'ZFS_PROP_WRITTEN',
    'ZFS_PROP_CLONES',
    'ZFS_PROP_LOGICALUSED',
    'ZFS_PROP_LOGICALREFERENCED',
    'ZFS_PROP_INCONSISTENT',
    'ZFS_PROP_FILESYSTEM_LIMIT',
    'ZFS_PROP_SNAPSHOT_LIMIT',
    'ZFS_PROP_FILESYSTEM_COUNT',
    'ZFS_PROP_SNAPSHOT_COUNT',
    'ZFS_PROP_SNAPDEV',
    'ZFS_PROP_ACLTYPE',
    'ZFS_PROP_SELINUX_CONTEXT',
    'ZFS_PROP_SELINUX_FSCONTEXT',
    'ZFS_PROP_SELINUX_DEFCONTEXT',
    'ZFS_PROP_SELINUX_ROOTCONTEXT',
    'ZFS_PROP_RELATIME',
    'ZFS_PROP_REDUNDANT_METADATA',
    'ZFS_PROP_OVERLAY',
    'ZFS_NUM_PROPS',
], start=0)

ffi.cdef('''
/*
 * Dataset properties are identified by these constants and must be added to
 * the end of this list to ensure that external consumers are not affected
 * by the change. If you make any changes to this list, be sure to update
 * the property table in module/zcommon/zfs_prop.c.
 */
typedef enum {
    ZFS_PROP_TYPE,
    ZFS_PROP_CREATION,
    ZFS_PROP_USED,
    ZFS_PROP_AVAILABLE,
    ZFS_PROP_REFERENCED,
    ZFS_PROP_COMPRESSRATIO,
    ZFS_PROP_MOUNTED,
    ZFS_PROP_ORIGIN,
    ZFS_PROP_QUOTA,
    ZFS_PROP_RESERVATION,
    ZFS_PROP_VOLSIZE,
    ZFS_PROP_VOLBLOCKSIZE,
    ZFS_PROP_RECORDSIZE,
    ZFS_PROP_MOUNTPOINT,
    ZFS_PROP_SHARENFS,
    ZFS_PROP_CHECKSUM,
    ZFS_PROP_COMPRESSION,
    ZFS_PROP_ATIME,
    ZFS_PROP_DEVICES,
    ZFS_PROP_EXEC,
    ZFS_PROP_SETUID,
    ZFS_PROP_READONLY,
    ZFS_PROP_ZONED,
    ZFS_PROP_SNAPDIR,
    ZFS_PROP_PRIVATE,       /* not exposed to user, temporary */
    ZFS_PROP_ACLINHERIT,
    ZFS_PROP_CREATETXG,     /* not exposed to the user */
    ZFS_PROP_NAME,          /* not exposed to the user */
    ZFS_PROP_CANMOUNT,
    ZFS_PROP_ISCSIOPTIONS,      /* not exposed to the user */
    ZFS_PROP_XATTR,
    ZFS_PROP_NUMCLONES,     /* not exposed to the user */
    ZFS_PROP_COPIES,
    ZFS_PROP_VERSION,
    ZFS_PROP_UTF8ONLY,
    ZFS_PROP_NORMALIZE,
    ZFS_PROP_CASE,
    ZFS_PROP_VSCAN,
    ZFS_PROP_NBMAND,
    ZFS_PROP_SHARESMB,
    ZFS_PROP_REFQUOTA,
    ZFS_PROP_REFRESERVATION,
    ZFS_PROP_GUID,
    ZFS_PROP_PRIMARYCACHE,
    ZFS_PROP_SECONDARYCACHE,
    ZFS_PROP_USEDSNAP,
    ZFS_PROP_USEDDS,
    ZFS_PROP_USEDCHILD,
    ZFS_PROP_USEDREFRESERV,
    ZFS_PROP_USERACCOUNTING,    /* not exposed to the user */
    ZFS_PROP_STMF_SHAREINFO,    /* not exposed to the user */
    ZFS_PROP_DEFER_DESTROY,
    ZFS_PROP_USERREFS,
    ZFS_PROP_LOGBIAS,
    ZFS_PROP_UNIQUE,        /* not exposed to the user */
    ZFS_PROP_OBJSETID,      /* not exposed to the user */
    ZFS_PROP_DEDUP,
    ZFS_PROP_MLSLABEL,
    ZFS_PROP_SYNC,
    ZFS_PROP_REFRATIO,
    ZFS_PROP_WRITTEN,
    ZFS_PROP_CLONES,
    ZFS_PROP_LOGICALUSED,
    ZFS_PROP_LOGICALREFERENCED,
    ZFS_PROP_INCONSISTENT,      /* not exposed to the user */
    ZFS_PROP_FILESYSTEM_LIMIT,
    ZFS_PROP_SNAPSHOT_LIMIT,
    ZFS_PROP_FILESYSTEM_COUNT,
    ZFS_PROP_SNAPSHOT_COUNT,
    ZFS_PROP_SNAPDEV,
    ZFS_PROP_ACLTYPE,
    ZFS_PROP_SELINUX_CONTEXT,
    ZFS_PROP_SELINUX_FSCONTEXT,
    ZFS_PROP_SELINUX_DEFCONTEXT,
    ZFS_PROP_SELINUX_ROOTCONTEXT,
    ZFS_PROP_RELATIME,
    ZFS_PROP_REDUNDANT_METADATA,
    ZFS_PROP_OVERLAY,
    ZFS_NUM_PROPS
} zfs_prop_t;
''')

zfs_userquota_prop_t = IntEnum('zfs_userquota_prop_t', [
    'ZFS_PROP_USERUSED',
    'ZFS_PROP_USERQUOTA',
    'ZFS_PROP_GROUPUSED',
    'ZFS_PROP_GROUPQUOTA',
    'ZFS_NUM_USERQUOTA_PROPS',
], start=0)

ffi.cdef('''
typedef enum {
    ZFS_PROP_USERUSED,
    ZFS_PROP_USERQUOTA,
    ZFS_PROP_GROUPUSED,
    ZFS_PROP_GROUPQUOTA,
    ZFS_NUM_USERQUOTA_PROPS
} zfs_userquota_prop_t;
''')

zpool_prop_t = IntEnum('zpool_prop_t', [
    'ZPOOL_PROP_NAME',
    'ZPOOL_PROP_SIZE',
    'ZPOOL_PROP_CAPACITY',
    'ZPOOL_PROP_ALTROOT',
    'ZPOOL_PROP_HEALTH',
    'ZPOOL_PROP_GUID',
    'ZPOOL_PROP_VERSION',
    'ZPOOL_PROP_BOOTFS',
    'ZPOOL_PROP_DELEGATION',
    'ZPOOL_PROP_AUTOREPLACE',
    'ZPOOL_PROP_CACHEFILE',
    'ZPOOL_PROP_FAILUREMODE',
    'ZPOOL_PROP_LISTSNAPS',
    'ZPOOL_PROP_AUTOEXPAND',
    'ZPOOL_PROP_DEDUPDITTO',
    'ZPOOL_PROP_DEDUPRATIO',
    'ZPOOL_PROP_FREE',
    'ZPOOL_PROP_ALLOCATED',
    'ZPOOL_PROP_READONLY',
    'ZPOOL_PROP_ASHIFT',
    'ZPOOL_PROP_COMMENT',
    'ZPOOL_PROP_EXPANDSZ',
    'ZPOOL_PROP_FREEING',
    'ZPOOL_PROP_FRAGMENTATION',
    'ZPOOL_PROP_LEAKED',
    'ZPOOL_PROP_MAXBLOCKSIZE',
    'ZPOOL_PROP_TNAME',
    'ZPOOL_NUM_PROPS'
], start=0)

ffi.cdef('''
/*
 * Pool properties are identified by these constants and must be added to the
 * end of this list to ensure that external consumers are not affected
 * by the change. If you make any changes to this list, be sure to update
 * the property table in module/zcommon/zpool_prop.c.
 */
typedef enum {
    ZPOOL_PROP_NAME,
    ZPOOL_PROP_SIZE,
    ZPOOL_PROP_CAPACITY,
    ZPOOL_PROP_ALTROOT,
    ZPOOL_PROP_HEALTH,
    ZPOOL_PROP_GUID,
    ZPOOL_PROP_VERSION,
    ZPOOL_PROP_BOOTFS,
    ZPOOL_PROP_DELEGATION,
    ZPOOL_PROP_AUTOREPLACE,
    ZPOOL_PROP_CACHEFILE,
    ZPOOL_PROP_FAILUREMODE,
    ZPOOL_PROP_LISTSNAPS,
    ZPOOL_PROP_AUTOEXPAND,
    ZPOOL_PROP_DEDUPDITTO,
    ZPOOL_PROP_DEDUPRATIO,
    ZPOOL_PROP_FREE,
    ZPOOL_PROP_ALLOCATED,
    ZPOOL_PROP_READONLY,
    ZPOOL_PROP_ASHIFT,
    ZPOOL_PROP_COMMENT,
    ZPOOL_PROP_EXPANDSZ,
    ZPOOL_PROP_FREEING,
    ZPOOL_PROP_FRAGMENTATION,
    ZPOOL_PROP_LEAKED,
    ZPOOL_PROP_MAXBLOCKSIZE,
    ZPOOL_PROP_TNAME,
    ZPOOL_NUM_PROPS
} zpool_prop_t;
''')


class zprop_source_t(IntEnum):
    ZPROP_SRC_NONE = 0x1
    ZPROP_SRC_DEFAULT = 0x2
    ZPROP_SRC_TEMPORARY = 0x4
    ZPROP_SRC_LOCAL = 0x8
    ZPROP_SRC_INHERITED = 0x10
    ZPROP_SRC_RECEIVED = 0x20


ffi.cdef('''
typedef enum {
    ZPROP_SRC_NONE = 0x1,
    ZPROP_SRC_DEFAULT = 0x2,
    ZPROP_SRC_TEMPORARY = 0x4,
    ZPROP_SRC_LOCAL = 0x8,
    ZPROP_SRC_INHERITED = 0x10,
    ZPROP_SRC_RECEIVED = 0x20
} zprop_source_t;
''')

zpool_status_t = IntEnum('zpool_status_t', [
    # The following correspond to faults as defined in the (fault.fs.zfs.*)
    # event namespace.  Each is associated with a corresponding message ID.
    'ZPOOL_STATUS_CORRUPT_CACHE',  # corrupt /kernel/drv/zpool.cache
    'ZPOOL_STATUS_MISSING_DEV_R',  # missing device with replicas
    'ZPOOL_STATUS_MISSING_DEV_NR',  # missing device with no replicas
    'ZPOOL_STATUS_CORRUPT_LABEL_R',  # bad device label with replicas
    'ZPOOL_STATUS_CORRUPT_LABEL_NR',  # bad device label with no replicas
    'ZPOOL_STATUS_BAD_GUID_SUM',  # sum of device guids didn't match
    'ZPOOL_STATUS_CORRUPT_POOL',  # pool metadata is corrupted
    'ZPOOL_STATUS_CORRUPT_DATA',  # data errors in user (meta)data
    'ZPOOL_STATUS_FAILING_DEV',  # device experiencing errors
    'ZPOOL_STATUS_VERSION_NEWER',  # newer on-disk version
    'ZPOOL_STATUS_HOSTID_MISMATCH',  # last accessed by another system
    'ZPOOL_STATUS_IO_FAILURE_WAIT',  # failed I/O, failmode 'wait'
    'ZPOOL_STATUS_IO_FAILURE_CONTINUE',  # failed I/O, failmode 'continue'
    'ZPOOL_STATUS_BAD_LOG',  # cannot read log chain(s)
    # If the pool has unsupported features but can still be opened in
    # read-only mode, its status is 'ZPOOL_STATUS_UNSUP_FEAT_WRITE.' If the
    # pool has unsupported features but cannot be opened at all, its
    # status is 'ZPOOL_STATUS_UNSUP_FEAT_READ.'
    'ZPOOL_STATUS_UNSUP_FEAT_READ',  # unsupported features for read
    'ZPOOL_STATUS_UNSUP_FEAT_WRITE',  # unsupported features for write
    # These faults have no corresponding message ID.  At the time we are
    # checking the status, the original reason for the FMA fault (I/O or
    # checksum errors) has been lost.
    'ZPOOL_STATUS_FAULTED_DEV_R',  # faulted device with replicas
    'ZPOOL_STATUS_FAULTED_DEV_NR',  # faulted device with no replicas
    # The following are not faults per se, but still an error possibly
    # requiring administrative attention.  There is no corresponding
    # message ID.
    'ZPOOL_STATUS_VERSION_OLDER',  # older legacy on-disk version
    'ZPOOL_STATUS_FEAT_DISABLED',  # supported features are disabled
    'ZPOOL_STATUS_RESILVERING',  # device being resilvered
    'ZPOOL_STATUS_OFFLINE_DEV',  # device online
    'ZPOOL_STATUS_REMOVED_DEV',  # removed device
    # Finally, the following indicates a healthy pool.
    'ZPOOL_STATUS_OK',
], start=0)

"""
ffi.cdef('''
/*
 * Pool health statistics.
 */
typedef enum {
    /*
     * The following correspond to faults as defined in the (fault.fs.zfs.*)
     * event namespace.  Each is associated with a corresponding message ID.
     */
    ZPOOL_STATUS_CORRUPT_CACHE,	/* corrupt /kernel/drv/zpool.cache */
    ZPOOL_STATUS_MISSING_DEV_R,	/* missing device with replicas */
    ZPOOL_STATUS_MISSING_DEV_NR,	/* missing device with no replicas */
    ZPOOL_STATUS_CORRUPT_LABEL_R,	/* bad device label with replicas */
    ZPOOL_STATUS_CORRUPT_LABEL_NR,	/* bad device label with no replicas */
    ZPOOL_STATUS_BAD_GUID_SUM,	/* sum of device guids didn't match */
    ZPOOL_STATUS_CORRUPT_POOL,	/* pool metadata is corrupted */
    ZPOOL_STATUS_CORRUPT_DATA,	/* data errors in user (meta)data */
    ZPOOL_STATUS_FAILING_DEV,	/* device experiencing errors */
    ZPOOL_STATUS_VERSION_NEWER,	/* newer on-disk version */
    ZPOOL_STATUS_HOSTID_MISMATCH,	/* last accessed by another system */
    ZPOOL_STATUS_IO_FAILURE_WAIT,	/* failed I/O, failmode 'wait' */
    ZPOOL_STATUS_IO_FAILURE_CONTINUE, /* failed I/O, failmode 'continue' */
    ZPOOL_STATUS_BAD_LOG,		/* cannot read log chain(s) */

    /*
     * If the pool has unsupported features but can still be opened in
     * read-only mode, its status is ZPOOL_STATUS_UNSUP_FEAT_WRITE. If the
     * pool has unsupported features but cannot be opened at all, its
     * status is ZPOOL_STATUS_UNSUP_FEAT_READ.
     */
    ZPOOL_STATUS_UNSUP_FEAT_READ,	/* unsupported features for read */
    ZPOOL_STATUS_UNSUP_FEAT_WRITE,	/* unsupported features for write */

    /*
     * These faults have no corresponding message ID.  At the time we are
     * checking the status, the original reason for the FMA fault (I/O or
     * checksum errors) has been lost.
     */
    ZPOOL_STATUS_FAULTED_DEV_R,	/* faulted device with replicas */
    ZPOOL_STATUS_FAULTED_DEV_NR,	/* faulted device with no replicas */

    /*
     * The following are not faults per se, but still an error possibly
     * requiring administrative attention.  There is no corresponding
     * message ID.
     */
    ZPOOL_STATUS_VERSION_OLDER,	/* older legacy on-disk version */
    ZPOOL_STATUS_FEAT_DISABLED,	/* supported features are disabled */
    ZPOOL_STATUS_RESILVERING,	/* device being resilvered */
    ZPOOL_STATUS_OFFLINE_DEV,	/* device online */
    ZPOOL_STATUS_REMOVED_DEV,	/* removed device */

    /*
     * Finally, the following indicates a healthy pool.
     */
    ZPOOL_STATUS_OK
} zpool_status_t;
''')
"""

pool_state_t = IntEnum('pool_state_t', [
    'POOL_STATE_ACTIVE',  # In active use
    'POOL_STATE_EXPORTED',  # Explicitly exported
    'POOL_STATE_DESTROYED',  # Explicitly destroyed
    'POOL_STATE_SPARE',  # Reserved for hot spare use
    'POOL_STATE_L2CACHE',  # Level 2 ARC device
    'POOL_STATE_UNINITIALIZED',  # Internal spa_t state
    'POOL_STATE_UNAVAIL',  # Internal libzfs state
    'POOL_STATE_POTENTIALLY_ACTIVE'  # Internal libzfs state
], start=0)

""" C defs """

ffi.cdef('''
typedef struct { ...; } avl_tree_t;
typedef struct { ...; } avl_node_t;
''')

"""
ffi.cdef('''
/*
 * The following data structures are all part
 * of the zfs_allow_t data structure which is
 * used for printing 'allow' permissions.
 * It is a linked list of zfs_allow_t's which
 * then contain avl tree's for user/group/sets/...
 * and each one of the entries in those trees have
 * avl tree's for the permissions they belong to and
 * whether they are local,descendent or local+descendent
 * permissions.  The AVL trees are used primarily for
 * sorting purposes, but also so that we can quickly find
 * a given user and or permission.
 */

typedef struct zfs_perm_node {
    avl_node_t z_node;
    char z_pname[];
} zfs_perm_node_t;

typedef struct zfs_allow_node {
    avl_node_t z_node;
    char z_key[];		/* name, such as joe */
    avl_tree_t z_localdescend;	/* local+descendent perms */
    avl_tree_t z_local;		/* local permissions */
    avl_tree_t z_descend;		/* descendent permissions */
} zfs_allow_node_t;

typedef struct zfs_allow {
    struct zfs_allow *z_next;
    char z_setpoint[];
    avl_tree_t z_sets;
    avl_tree_t z_crperms;
    avl_tree_t z_user;
    avl_tree_t z_group;
    avl_tree_t z_everyone;
} zfs_allow_t;
''')
"""

# ffi.cdef('''
# typedef ... zfs_handle_t;
# typedef ... zpool_handle_t;
# typedef ... libzfs_handle_t;
# ''')

"""
ffi.cdef('''
typedef struct splitflags {
    /* do not split, but return the config that would be split off */
    int dryrun : 1;

    /* after splitting, import the pool */
    int import : 1;
} splitflags_t;
''')
"""

"""
ffi.cdef('''
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
''')

ffi.cdef('''
typedef struct zprop_list {
    int		pl_prop;
    char		*pl_user_prop;
    struct zprop_list *pl_next;
    boolean_t	pl_all;
    size_t		pl_width;
    size_t		pl_recvd_width;
    boolean_t	pl_fixed;
} zprop_list_t;
''')

ffi.cdef('''
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
    zfs_get_column_t cb_columns[5];
    int cb_colwidths[6];
    boolean_t cb_scripted;
    boolean_t cb_literal;
    boolean_t cb_first;
    zprop_list_t *cb_proplist;
    zfs_type_t cb_type;
} zprop_get_cbdata_t;

typedef struct get_all_cb {
    zfs_handle_t	**cb_handles;
    size_t		cb_alloc;
    size_t		cb_used;
    boolean_t	cb_verbose;
    int		(*cb_getone)(zfs_handle_t *, void *);
} get_all_cb_t;


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
''')
"""

ffi.cdef('''
typedef enum {
    ZFS_TYPE_FILESYSTEM	= 0x1,
    ZFS_TYPE_SNAPSHOT	= 0x2,
    ZFS_TYPE_VOLUME		= 0x4,
    ZFS_TYPE_POOL		= 0x8
} zfs_type_t;
''')

""" From sys/fs/zfs.h """


class zfs_type_t(IntEnum):
    """ Each dataset can be one of the following types.  These constants can be
    combined into masks that can be passed to various functions. """
    ZFS_TYPE_FILESYSTEM = 1
    ZFS_TYPE_SNAPSHOT = 2
    ZFS_TYPE_VOLUME = 4
    ZFS_TYPE_POOL = 8

    DATASET = ZFS_TYPE_FILESYSTEM | ZFS_TYPE_SNAPSHOT | ZFS_TYPE_VOLUME
    ALL = DATASET | ZFS_TYPE_POOL


ffi.cdef('typedef enum vdev_state { ... } vdev_state_t;')
ffi.cdef('typedef enum vdev_aux { ... } vdev_aux_t;')
ffi.cdef('typedef enum pool_state { ... } pool_state_t;')
ffi.cdef('typedef enum pool_scan_func { ... } pool_scan_func_t;')
ffi.cdef('typedef enum zio_type { ... } zio_type_T;')
ffi.cdef('typedef enum pool_scan_stat { ... } pool_scan_stat_t;')
ffi.cdef('typedef enum zpool_errata { ... } zpool_errata_t;')
ffi.cdef('typedef enum vdev_stat { ... } vdev_stat_t;')
ffi.cdef('typedef enum zfs_ioc { ... } zfs_ioc_t;')

ffi.cdef('''
typedef enum {
    ZPROP_ERR_NOCLEAR = 0x1, /* failure to clear existing props */
    ZPROP_ERR_NORESTORE = 0x2 /* failure to restore props on error */
} zprop_errflags_t;

typedef int (*zprop_func)(int, void *);
''')
