from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(name='functions',
      ext_modules=cythonize("build/core_func.pyx"),
      include_dirs=[numpy.get_include()])
