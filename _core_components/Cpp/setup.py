from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

ext = Extension('cpp_func', sources=["cpp_func.pyx"], language="c++")
setup(name="cpp_func", ext_modules=cythonize([ext]))