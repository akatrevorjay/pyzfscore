
from .. import _cffi, libnvpair
from .._cffi import verify

from cffi import FFI
ffi = FFI()
ffi.include(_cffi.ffi)
ffi.include(libnvpair.ffi)
