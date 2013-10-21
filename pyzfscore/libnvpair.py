
from .flufl.enum import IntEnum
from . import _cffi


from cffi import FFI
ffi = FFI()
ffi.include(_cffi.ffi)


data_type_t = IntEnum('data_type_t', [
	'DATA_TYPE_UNKNOWN',
	'DATA_TYPE_BOOLEAN',
	'DATA_TYPE_BYTE',
	'DATA_TYPE_INT16',
	'DATA_TYPE_UINT16',
	'DATA_TYPE_INT32',
	'DATA_TYPE_UINT32',
	'DATA_TYPE_INT64',
	'DATA_TYPE_UINT64',
	'DATA_TYPE_STRING',
	'DATA_TYPE_BYTE_ARRAY',
	'DATA_TYPE_INT16_ARRAY',
	'DATA_TYPE_UINT16_ARRAY',
	'DATA_TYPE_INT32_ARRAY',
	'DATA_TYPE_UINT32_ARRAY',
	'DATA_TYPE_INT64_ARRAY',
	'DATA_TYPE_UINT64_ARRAY',
	'DATA_TYPE_STRING_ARRAY',
	'DATA_TYPE_HRTIME',
	'DATA_TYPE_NVLIST',
	'DATA_TYPE_NVLIST_ARRAY',
	'DATA_TYPE_BOOLEAN_VALUE',
	'DATA_TYPE_INT8',
	'DATA_TYPE_UINT8',
	'DATA_TYPE_BOOLEAN_ARRAY',
	'DATA_TYPE_INT8_ARRAY',
	'DATA_TYPE_UINT8_ARRAY',
	'DATA_TYPE_DOUBLE',
], start=0)


ffi.cdef('''
typedef enum {
	DATA_TYPE_UNKNOWN = 0,
	DATA_TYPE_BOOLEAN,
	DATA_TYPE_BYTE,
	DATA_TYPE_INT16,
	DATA_TYPE_UINT16,
	DATA_TYPE_INT32,
	DATA_TYPE_UINT32,
	DATA_TYPE_INT64,
	DATA_TYPE_UINT64,
	DATA_TYPE_STRING,
	DATA_TYPE_BYTE_ARRAY,
	DATA_TYPE_INT16_ARRAY,
	DATA_TYPE_UINT16_ARRAY,
	DATA_TYPE_INT32_ARRAY,
	DATA_TYPE_UINT32_ARRAY,
	DATA_TYPE_INT64_ARRAY,
	DATA_TYPE_UINT64_ARRAY,
	DATA_TYPE_STRING_ARRAY,
	DATA_TYPE_HRTIME,
	DATA_TYPE_NVLIST,
	DATA_TYPE_NVLIST_ARRAY,
	DATA_TYPE_BOOLEAN_VALUE,
	DATA_TYPE_INT8,
	DATA_TYPE_UINT8,
	DATA_TYPE_BOOLEAN_ARRAY,
	DATA_TYPE_INT8_ARRAY,
	DATA_TYPE_UINT8_ARRAY,
	DATA_TYPE_DOUBLE
} data_type_t;
''')


ffi.cdef('''
typedef struct nvpair {
	int32_t nvp_size;	/* size of this nvpair */
	int16_t	nvp_name_sz;	/* length of name string */
	int16_t	nvp_reserve;	/* not used */
	int32_t	nvp_value_elem;	/* number of elements for array types */
	data_type_t nvp_type;	/* type of value */
	/* name string */
	/* aligned ptr array for string arrays */
	/* aligned array of data for value */
} nvpair_t;

/* nvlist header */
typedef struct nvlist {
	int32_t		nvl_version;
	uint32_t	nvl_nvflag;	/* persistent flags */
	uint64_t	nvl_priv;	/* ptr to private data if not packed */
	uint32_t	nvl_flag;
	int32_t		nvl_pad;	/* currently not used, for alignment */
} nvlist_t;
''')


ffi.cdef('''
/* NV allocator framework */
typedef struct nv_alloc_ops nv_alloc_ops_t;

typedef struct nv_alloc {
	const nv_alloc_ops_t *nva_ops;
	void *nva_arg;
} nv_alloc_t;
''')


#ffi.cdef('void nvlist_print(FILE *, nvlist_t *);')
def nvlist_print(f, nvlist_t):
    return cnvpair.nvlist_print(f, nvlist_t)


#ffi.cdef('void dump_nvlist(nvlist_t *, int);')
def dump_nvlist(nvlist_t, i):
    return cnvpair.dump_nvlist(nvlist_t, i)


ffi.cdef('''
/* list management */
int nvlist_alloc(nvlist_t **, uint_t, int);
void nvlist_free(nvlist_t *);
int nvlist_size(nvlist_t *, size_t *, int);
int nvlist_pack(nvlist_t *, char **, size_t *, int, int);
int nvlist_unpack(char *, size_t, nvlist_t **, int);
int nvlist_dup(nvlist_t *, nvlist_t **, int);
int nvlist_merge(nvlist_t *, nvlist_t *, int);

uint_t nvlist_nvflag(nvlist_t *);

int nvlist_xalloc(nvlist_t **, uint_t, nv_alloc_t *);
int nvlist_xpack(nvlist_t *, char **, size_t *, int, nv_alloc_t *);
int nvlist_xunpack(char *, size_t, nvlist_t **, nv_alloc_t *);
int nvlist_xdup(nvlist_t *, nvlist_t **, nv_alloc_t *);
nv_alloc_t *nvlist_lookup_nv_alloc(nvlist_t *);

int nvlist_add_nvpair(nvlist_t *, nvpair_t *);
int nvlist_add_boolean(nvlist_t *, const char *);
int nvlist_add_boolean_value(nvlist_t *, const char *, boolean_t);
int nvlist_add_byte(nvlist_t *, const char *, uchar_t);
int nvlist_add_int8(nvlist_t *, const char *, int8_t);
int nvlist_add_uint8(nvlist_t *, const char *, uint8_t);
int nvlist_add_int16(nvlist_t *, const char *, int16_t);
int nvlist_add_uint16(nvlist_t *, const char *, uint16_t);
int nvlist_add_int32(nvlist_t *, const char *, int32_t);
int nvlist_add_uint32(nvlist_t *, const char *, uint32_t);
int nvlist_add_int64(nvlist_t *, const char *, int64_t);
int nvlist_add_uint64(nvlist_t *, const char *, uint64_t);
int nvlist_add_string(nvlist_t *, const char *, const char *);
int nvlist_add_nvlist(nvlist_t *, const char *, nvlist_t *);
int nvlist_add_boolean_array(nvlist_t *, const char *, boolean_t *, uint_t);
int nvlist_add_byte_array(nvlist_t *, const char *, uchar_t *, uint_t);
int nvlist_add_int8_array(nvlist_t *, const char *, int8_t *, uint_t);
int nvlist_add_uint8_array(nvlist_t *, const char *, uint8_t *, uint_t);
int nvlist_add_int16_array(nvlist_t *, const char *, int16_t *, uint_t);
int nvlist_add_uint16_array(nvlist_t *, const char *, uint16_t *, uint_t);
int nvlist_add_int32_array(nvlist_t *, const char *, int32_t *, uint_t);
int nvlist_add_uint32_array(nvlist_t *, const char *, uint32_t *, uint_t);
int nvlist_add_int64_array(nvlist_t *, const char *, int64_t *, uint_t);
int nvlist_add_uint64_array(nvlist_t *, const char *, uint64_t *, uint_t);
int nvlist_add_string_array(nvlist_t *, const char *, char *const *, uint_t);
int nvlist_add_nvlist_array(nvlist_t *, const char *, nvlist_t **, uint_t);
int nvlist_add_hrtime(nvlist_t *, const char *, hrtime_t);
int nvlist_add_double(nvlist_t *, const char *, double);

int nvlist_remove(nvlist_t *, const char *, data_type_t);
int nvlist_remove_all(nvlist_t *, const char *);
int nvlist_remove_nvpair(nvlist_t *, nvpair_t *);

int nvlist_lookup_boolean(nvlist_t *, const char *);
int nvlist_lookup_boolean_value(nvlist_t *, const char *, boolean_t *);
int nvlist_lookup_byte(nvlist_t *, const char *, uchar_t *);
int nvlist_lookup_int8(nvlist_t *, const char *, int8_t *);
int nvlist_lookup_uint8(nvlist_t *, const char *, uint8_t *);
int nvlist_lookup_int16(nvlist_t *, const char *, int16_t *);
int nvlist_lookup_uint16(nvlist_t *, const char *, uint16_t *);
int nvlist_lookup_int32(nvlist_t *, const char *, int32_t *);
int nvlist_lookup_uint32(nvlist_t *, const char *, uint32_t *);
int nvlist_lookup_int64(nvlist_t *, const char *, int64_t *);
int nvlist_lookup_uint64(nvlist_t *, const char *, uint64_t *);
int nvlist_lookup_string(nvlist_t *, const char *, char **);
int nvlist_lookup_nvlist(nvlist_t *, const char *, nvlist_t **);
int nvlist_lookup_boolean_array(nvlist_t *, const char *,
    boolean_t **, uint_t *);
int nvlist_lookup_byte_array(nvlist_t *, const char *, uchar_t **, uint_t *);
int nvlist_lookup_int8_array(nvlist_t *, const char *, int8_t **, uint_t *);
int nvlist_lookup_uint8_array(nvlist_t *, const char *, uint8_t **, uint_t *);
int nvlist_lookup_int16_array(nvlist_t *, const char *, int16_t **, uint_t *);
int nvlist_lookup_uint16_array(nvlist_t *, const char *, uint16_t **, uint_t *);
int nvlist_lookup_int32_array(nvlist_t *, const char *, int32_t **, uint_t *);
int nvlist_lookup_uint32_array(nvlist_t *, const char *, uint32_t **, uint_t *);
int nvlist_lookup_int64_array(nvlist_t *, const char *, int64_t **, uint_t *);
int nvlist_lookup_uint64_array(nvlist_t *, const char *, uint64_t **, uint_t *);
int nvlist_lookup_string_array(nvlist_t *, const char *, char ***, uint_t *);
int nvlist_lookup_nvlist_array(nvlist_t *, const char *,
    nvlist_t ***, uint_t *);
int nvlist_lookup_hrtime(nvlist_t *, const char *, hrtime_t *);
int nvlist_lookup_pairs(nvlist_t *, int, ...);
int nvlist_lookup_double(nvlist_t *, const char *, double *);

int nvlist_lookup_nvpair(nvlist_t *, const char *, nvpair_t **);
int nvlist_lookup_nvpair_embedded_index(nvlist_t *, const char *, nvpair_t **,
    int *, char **);
boolean_t nvlist_exists(nvlist_t *, const char *);
boolean_t nvlist_empty(nvlist_t *);

/* processing nvpair */
nvpair_t *nvlist_next_nvpair(nvlist_t *, nvpair_t *);
nvpair_t *nvlist_prev_nvpair(nvlist_t *, nvpair_t *);
char *nvpair_name(nvpair_t *);
data_type_t nvpair_type(nvpair_t *);
int nvpair_type_is_array(nvpair_t *);
int nvpair_value_boolean_value(nvpair_t *, boolean_t *);
int nvpair_value_byte(nvpair_t *, uchar_t *);
int nvpair_value_int8(nvpair_t *, int8_t *);
int nvpair_value_uint8(nvpair_t *, uint8_t *);
int nvpair_value_int16(nvpair_t *, int16_t *);
int nvpair_value_uint16(nvpair_t *, uint16_t *);
int nvpair_value_int32(nvpair_t *, int32_t *);
int nvpair_value_uint32(nvpair_t *, uint32_t *);
int nvpair_value_int64(nvpair_t *, int64_t *);
int nvpair_value_uint64(nvpair_t *, uint64_t *);
int nvpair_value_string(nvpair_t *, char **);
int nvpair_value_nvlist(nvpair_t *, nvlist_t **);
int nvpair_value_boolean_array(nvpair_t *, boolean_t **, uint_t *);
int nvpair_value_byte_array(nvpair_t *, uchar_t **, uint_t *);
int nvpair_value_int8_array(nvpair_t *, int8_t **, uint_t *);
int nvpair_value_uint8_array(nvpair_t *, uint8_t **, uint_t *);
int nvpair_value_int16_array(nvpair_t *, int16_t **, uint_t *);
int nvpair_value_uint16_array(nvpair_t *, uint16_t **, uint_t *);
int nvpair_value_int32_array(nvpair_t *, int32_t **, uint_t *);
int nvpair_value_uint32_array(nvpair_t *, uint32_t **, uint_t *);
int nvpair_value_int64_array(nvpair_t *, int64_t **, uint_t *);
int nvpair_value_uint64_array(nvpair_t *, uint64_t **, uint_t *);
int nvpair_value_string_array(nvpair_t *, char ***, uint_t *);
int nvpair_value_nvlist_array(nvpair_t *, nvlist_t ***, uint_t *);
int nvpair_value_hrtime(nvpair_t *, hrtime_t *);
int nvpair_value_double(nvpair_t *, double *);

nvlist_t *fnvlist_alloc(void);
void fnvlist_free(nvlist_t *);
size_t fnvlist_size(nvlist_t *);
char *fnvlist_pack(nvlist_t *, size_t *);
void fnvlist_pack_free(char *, size_t);
nvlist_t *fnvlist_unpack(char *, size_t);
nvlist_t *fnvlist_dup(nvlist_t *);
void fnvlist_merge(nvlist_t *, nvlist_t *);

void fnvlist_add_boolean(nvlist_t *, const char *);
void fnvlist_add_boolean_value(nvlist_t *, const char *, boolean_t);
void fnvlist_add_byte(nvlist_t *, const char *, uchar_t);
void fnvlist_add_int8(nvlist_t *, const char *, int8_t);
void fnvlist_add_uint8(nvlist_t *, const char *, uint8_t);
void fnvlist_add_int16(nvlist_t *, const char *, int16_t);
void fnvlist_add_uint16(nvlist_t *, const char *, uint16_t);
void fnvlist_add_int32(nvlist_t *, const char *, int32_t);
void fnvlist_add_uint32(nvlist_t *, const char *, uint32_t);
void fnvlist_add_int64(nvlist_t *, const char *, int64_t);
void fnvlist_add_uint64(nvlist_t *, const char *, uint64_t);
void fnvlist_add_string(nvlist_t *, const char *, const char *);
void fnvlist_add_nvlist(nvlist_t *, const char *, nvlist_t *);
void fnvlist_add_nvpair(nvlist_t *, nvpair_t *);
void fnvlist_add_boolean_array(nvlist_t *, const char *, boolean_t *, uint_t);
void fnvlist_add_byte_array(nvlist_t *, const char *, uchar_t *, uint_t);
void fnvlist_add_int8_array(nvlist_t *, const char *, int8_t *, uint_t);
void fnvlist_add_uint8_array(nvlist_t *, const char *, uint8_t *, uint_t);
void fnvlist_add_int16_array(nvlist_t *, const char *, int16_t *, uint_t);
void fnvlist_add_uint16_array(nvlist_t *, const char *, uint16_t *, uint_t);
void fnvlist_add_int32_array(nvlist_t *, const char *, int32_t *, uint_t);
void fnvlist_add_uint32_array(nvlist_t *, const char *, uint32_t *, uint_t);
void fnvlist_add_int64_array(nvlist_t *, const char *, int64_t *, uint_t);
void fnvlist_add_uint64_array(nvlist_t *, const char *, uint64_t *, uint_t);
void fnvlist_add_string_array(nvlist_t *, const char *, char * const *, uint_t);
void fnvlist_add_nvlist_array(nvlist_t *, const char *, nvlist_t **, uint_t);

void fnvlist_remove(nvlist_t *, const char *);
void fnvlist_remove_nvpair(nvlist_t *, nvpair_t *);

nvpair_t *fnvlist_lookup_nvpair(nvlist_t *nvl, const char *name);
boolean_t fnvlist_lookup_boolean(nvlist_t *nvl, const char *name);
boolean_t fnvlist_lookup_boolean_value(nvlist_t *nvl, const char *name);
uchar_t fnvlist_lookup_byte(nvlist_t *nvl, const char *name);
int8_t fnvlist_lookup_int8(nvlist_t *nvl, const char *name);
int16_t fnvlist_lookup_int16(nvlist_t *nvl, const char *name);
int32_t fnvlist_lookup_int32(nvlist_t *nvl, const char *name);
int64_t fnvlist_lookup_int64(nvlist_t *nvl, const char *name);
uint8_t fnvlist_lookup_uint8(nvlist_t *nvl, const char *name);
uint16_t fnvlist_lookup_uint16(nvlist_t *nvl, const char *name);
uint32_t fnvlist_lookup_uint32(nvlist_t *nvl, const char *name);
uint64_t fnvlist_lookup_uint64(nvlist_t *nvl, const char *name);
char *fnvlist_lookup_string(nvlist_t *nvl, const char *name);
nvlist_t *fnvlist_lookup_nvlist(nvlist_t *nvl, const char *name);

boolean_t fnvpair_value_boolean_value(nvpair_t *nvp);
uchar_t fnvpair_value_byte(nvpair_t *nvp);
int8_t fnvpair_value_int8(nvpair_t *nvp);
int16_t fnvpair_value_int16(nvpair_t *nvp);
int32_t fnvpair_value_int32(nvpair_t *nvp);
int64_t fnvpair_value_int64(nvpair_t *nvp);
uint8_t fnvpair_value_uint8(nvpair_t *nvp);
uint16_t fnvpair_value_uint16(nvpair_t *nvp);
uint32_t fnvpair_value_uint32(nvpair_t *nvp);
uint64_t fnvpair_value_uint64(nvpair_t *nvp);
char *fnvpair_value_string(nvpair_t *nvp);
nvlist_t *fnvpair_value_nvlist(nvpair_t *nvp);
''')


cnvpair = _cffi.verify(ffi)
