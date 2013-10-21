
from .. import _cffi, libnvpair
from .._cffi import verify, boolean_t

from cffi import FFI
ffi = FFI()
#ffi.include(_cffi.ffi)
ffi.include(libnvpair.ffi)
