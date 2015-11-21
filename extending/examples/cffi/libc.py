from cffi import FFI
ffi = FFI()
ffi.cdef("""
int printf(const char *format, ...);""")
C = ffi.dlopen(None)
arg = ffi.new("char[]", "world")
C.printf("hi there, %s!\n", arg)
