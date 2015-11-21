import cffi
ffi = cffi.FFI()

ffi.cdef("""
int fib(int n);
""")

lib = ffi.verify(r'''
int fib(int n){
  if ( n < 2 )
      return n;
  else
   return fib(n-1) + fib(n-2);
}''')

print lib.fib(10)
