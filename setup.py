#! /usr/bin/env python
"""
Part of PyZFSCore.

Copyright 2013 Trevor Joynson

"""

from setuptools import setup

import pyzfscore
import pyzfscore.libzfs
import pyzfscore.libnvpair

setup(
    name='pyzfscore',
    version='0.0.1',
    description='ZFS CFFI wrapper.',
    license='GPL3',
    maintainer='Trevor Joynson',
    maintainer_email='github@skywww.net',
    url='http://github.com/akatrevorjay/pyzfscore',
    packages=[
        'pyzfscore',
        'pyzfscore.libzfs',
        'pyzfscore.flufl',
        'pyzfscore.flufl.enum',
    ],
    install_requires=['cffi'],
    zip_safe=False,
    ext_modules=[
        pyzfscore.libzfs.ffi.verifier.get_extension(),
        pyzfscore.libnvpair.ffi.verifier.get_extension(),
    ],
)
