from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='functions',
    ext_modules=cythonize("movies.pyx"),
)