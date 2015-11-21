import ctypes

lib_algebra = ctypes.CDLL('./lib_algebra.so')
cbrd = lib_algebra.__lib_algebra_MOD_cbrt_sp
cbrd.restype = ctypes.c_float
cbrd.arguments = [ctypes.c_float, ctypes.c_float]

def cbrd_py(x, y):
    return cbrd(ctypes.c_float(x), ctypes.c_float(y))

print cbrd_py(2, 2)
