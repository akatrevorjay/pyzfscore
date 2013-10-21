#!/usr/bin/env python

import os
import inspect
from functools import wraps
from cffi import FFI


ffi = FFI()




def ptop(typ, val):
    ptop = ffi.new('%s*[1]' % typ)
    ptop[0] = val
    return ptop


def cdef(decl, returns_string=False, nullable=False, ffi=ffi):
    ffi.cdef(decl)
    def wrap(f):
        @wraps(f)
        def inner_f(*args):
            val = f(*args)
            # if Z.zmq_errno():
            #     raise Exception(os.strerror(Z.zmq_errno()))
            if nullable and val == ffi.NULL:
                return None
            elif returns_string:
                return ffi.string(val)
            return val

        # this insanity inserts a formatted argspec string
        # into the function's docstring, so that sphinx
        # gets the right args instead of just the wrapper args
        args, varargs, varkw, defaults = inspect.getargspec(f)
        defaults = () if defaults is None else defaults
        defaults = ["\"{}\"".format(a) if type(a) == str else a for a in defaults]
        l = ["{}={}".format(arg, defaults[(idx+1)*-1])
             if len(defaults)-1 >= idx else
             arg for idx, arg in enumerate(reversed(list(args)))]
        if varargs:
            l.append('*' + varargs)
        if varkw:
            l.append('**' + varkw)
        doc = "{}({})\n\nC: ``{}``\n\n{}".format(f.__name__, ', '.join(reversed(l)), decl, f.__doc__)
        inner_f.__doc__ = doc
        return inner_f
    return wrap


czfs = ffi.dlopen('zfs')
czpool = ffi.dlopen('zpool')
cnvpair = ffi.dlopen('nvpair')


ffi.cdef('typedef enum { B_FALSE, B_TRUE } boolean_t;')

def boolean_t(value=None):
    return ffi.cast('boolean_t', value)

ffi.cdef('''
typedef unsigned char	uchar_t;
typedef unsigned short	ushort_t;
typedef unsigned int	uint_t;
typedef unsigned long	ulong_t;
typedef long long	longlong_t;
typedef longlong_t	hrtime_t;
''')


def verify(ffi=ffi):
    return ffi.verify('''
    #include <libzfs.h>
    #include <sys/fs/zfs.h>
    #include <sys/types.h>
    #include <libnvpair.h>
    ''',
        define_macros=[
            ('NDEBUG', 1),
            ('HAVE_IOCTL_IN_SYS_IOCTL_H', 1)
        ],
        include_dirs=['/usr/include/libzfs', '/usr/include/libspl'],
        libraries=['nvpair', 'zfs', 'zpool'],
    )

    #return ffi.verify('''
    ##include <sys/avl.h>
    ##include <sys/fs/zfs.h>
    ##include <sys/types.h>
    ##include <sys/param.h>
    ##include <libzfs.h>
    ##include <libnvpair.h>
    #''',
    #    define_macros=[
    #        ('NDEBUG', 1),
    #        ('HAVE_IOCTL_IN_SYS_IOCTL_H', 1),
    #        ('PATH_MAX', 4096),
    #    ],
    #    include_dirs=['/usr/include/libzfs', '/usr/include/libspl'],
    #    libraries=['nvpair', 'zfs', 'zpool'],
    #)
