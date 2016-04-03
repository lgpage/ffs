import os
import sys
import glob
from setuptools import setup, Extension
from distutils.command.build_ext import build_ext

cython_directives = {
    'embedsignature': True,  # needed to embed docstrings in ext module
    }

try:
    sys.argv.remove("--use-cython")
    use_cython = True
except ValueError:
    use_cython = False

root = os.path.dirname(__file__)
if use_cython:
    ext_files = glob.glob(os.path.join(root, 'src', '*.pyx'))
    ext_files.append(os.path.join(root, 'src', 'pure_py_module.py'))
else:
    ext_files = glob.glob(os.path.join(root, 'src', '*.c'))

extensions = []
include_dirs = [os.path.abspath(os.path.join(root, 'clib'))]
for file_ in ext_files:
    pyx_file, ext = os.path.splitext(file_)
    extensions.append(Extension(pyx_file, [file_],
                                include_dirs=include_dirs))

if use_cython:
    from Cython.Build import cythonize
    extensions = cythonize(extensions, force=True,
                            compiler_directives=cython_directives)

setup(
    name="cythontests",
    version="0.1",
    description="build cython extension modules for pytest tests",
    ext_modules=extensions,
    cmdclass = {
        'build_ext': build_ext,
        }
    )
