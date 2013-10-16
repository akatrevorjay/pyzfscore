#!/usr/bin/env python

from _cffi import czfs, czpool, cnvpair, ptop, cdef, ffi


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
def zfs_open(zhp, name, arg=0):
    """Gets zfs_handle for dataset"""
    return ffi.gc(czfs.zfs_open(zhp, name, arg), zfs_close)


#@cdef('zfs_type_t zfs_get_type(const zfs_handle_t *);')
#def zfs_get_type(zhp):
#    """Gets type for zfs_handle"""
#    return czfs.zfs_get_type(zhp)


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

#define	ZFS_MOUNTPOINT_NONE	"none"
#define	ZFS_MOUNTPOINT_LEGACY	"legacy"

#define	ZFS_FEATURE_DISABLED	"disabled"
#define	ZFS_FEATURE_ENABLED	"enabled"
#define	ZFS_FEATURE_ACTIVE	"active"

#define	ZFS_UNSUPPORTED_INACTIVE	"inactive"
#define	ZFS_UNSUPPORTED_READONLY	"readonly"

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
''',
    define_macros=[
        ('NDEBUG', 1),
        ('HAVE_IOCTL_IN_SYS_IOCTL_H', 1)
    ],
    include_dirs=['/usr/include/libzfs', '/usr/include/libspl'],
    libraries=['nvpair', 'zfs', 'zpool'],
)



