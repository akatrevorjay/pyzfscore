#! /usr/bin/env python
"""
Part of PyZFSCore.

Copyright 2013 Trevor Joynson

"""
from setuptools import setup, Extension

libzfs_ext = Extension(
    name='libzfs',
    define_macros=[('NDEBUG', 1), ('HAVE_IOCTL_IN_SYS_IOCTL_H', 1)],
    libraries=['nvpair', 'zfs', 'zpool'],
    sources=['pyzfscore/__pycache__/_cffi__x8618e7c5xe2b6f166.c'],
    include_dirs=['/usr/include/libzfs', '/usr/include/libspl']
)

setup(
    name='pyzfscore',
    version='0.0.1',
    description='ZFS CFFI wrapper.',
    license='GPL3',
    author='Trevor Joynson',
    author_email='github@skywww.net',
    maintainer='Ben Cole',
    maintainer_email='wengole@gmail.com',
    url='http://github.com/wengole/pyzfscore',
    packages=[
        'pyzfscore',
        'pyzfscore.libzfs',
        'pyzfscore.flufl',
        'pyzfscore.flufl.enum',
    ],
    install_requires=['cffi'],
    zip_safe=False,
    ext_modules=[
        libzfs_ext
    ],
)
