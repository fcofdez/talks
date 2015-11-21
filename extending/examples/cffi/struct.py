from cffi import FFI
ffi = FFI()
ffi.cdef("""
typedef struct {
float x, y;
} point;
""")
point = ffi.new("point *")
point.x = 2.0
point.y = 3.0
print point
