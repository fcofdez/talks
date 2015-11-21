import ctypes

lib_newton = ctypes.CDLL('./lib_newton.so')
newton_c = lib_newton.newton
newton_c.restype = ctypes.c_float
newton_c.argtypes = [ctypes.c_float, ctypes.c_float]


def newton(guess, x):
    return newton_c(ctypes.c_float(guess), ctypes.c_float(x))

print newton(1, 2)
