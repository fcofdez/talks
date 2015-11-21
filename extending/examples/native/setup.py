from distutils.core import setup, Extension

setup(name='My newton',
      version=1.0,
      ext_modules=[Extension('newton', ['newton.c'])])
