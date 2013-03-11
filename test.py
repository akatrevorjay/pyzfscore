
import ctypes
from ctypes import *

import libnvpair
import libzfs
import zfs
from zfs import *
from libnvpair import *
from libzfs import *


dp = Zpool('dpool')
php = dp._handle
ph = php.contents


zh = libzfs.libzfs_init()
php2 = libzfs.zpool_open(zh, 'dpool')
ph2 = php2.contents

fshp = libzfs.zfs_open(zh, 'dpool/tmp', 1)
fsh = fshp[0]

# Prop Creation
zpth = zfs_prop_t(value=27)
#zpthp = pointer(zpth)

# Src None
zpsh = zprop_source_t(value=1)
#zpshp = pointer(zpsh)


a = zfs_prop_get(fsh,
    zpth, '', 0,
    zpsh, '', 0,
    True
)

print a


buf = create_unicode_buffer('', size=1024)
buf2 = c_char_p()

buf3 = ''
bufp = ctypes.pointer(buf)

a = zfs_prop_get_written(fsh,
    u'USED',
    #buf, sizeof(buf),
    #byref(buf2), 0,
    #buf, 1024,
    #bufp, 1024,
    buf,
    #c_size_t(buf),
    #c_int(value=1024),
    1024,
    1,
    #True,
    #False,
)

print a


