import os
import glob

from Cython.Build import cythonize
from Cython.Distutils import build_ext
from setuptools import setup, Extension

root = os.path.dirname(__file__)
ext_files = glob.glob(os.path.join(root, 'src', '*.pyx'))
ext_files.append(os.path.join(root, 'src', 'pure_py_module.py'))

extensions = []
include_dirs = [os.path.abspath(os.path.join(root, 'clib'))]
for file_ in ext_files:
    pyx_file, ext = os.path.splitext(file_)
    extensions.append(Extension(pyx_file, [file_],
                                include_dirs=include_dirs))

setup(
    name="cythontest",
    version="0.1",
    description="blarg",
    ext_modules=cythonize(extensions, force=True),
    zip_safe = False,
    cmdclass = {
        'build_ext': build_ext,
        },
    entry_points = {
        'console_scripts': [
            'cython = Cython.Compiler.Main:setuptools_main',
            'cythonize = Cython.Build.Cythonize:main',
            ],
        },
    )
