#!/usr/bin/env python
import os

# appdirs is a dependency of setuptools, so allow installing without it.
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import ast

# path for this script
_SCRIPT_PATH: str = os.path.dirname(__file__)
# app file name (assuming directory name matches app)
_APP_FILE: str = os.path.basename(_SCRIPT_PATH) + '.py'


def get_path(fname: str)-> str:
    """ Return full path of file <fname> in *current* script directory.

    `get_path(fname: str)-> str`

    """
    return os.path.join(_SCRIPT_PATH, fname)

def read(fname: str, nl: str = '\n')-> str:
    """ #### Return file contents with normalized line endings.

        `read(fname: str)-> str`

        Return text of file <fname> with line endings normalized to "\\n"

            fname:  str - name of file to process
            nl:     str - default newline string ('\\n')

            return: str - text of file <fname>
        """
    with open(get_path(fname)) as inf:
        out = nl + inf.read().replace("\r\n", nl)
    return out

def get_version(fname: str) -> str:
    """ #### Get version from file <fname>.

        `get_version(fname: str) -> str`

        """
    for line in read(fname).splitlines():
        if line.startswith("__version__"):
            version = ast.literal_eval(line.split("=", 1)[1].strip())
            return version
    return ''


# Do not import `appdirs` yet, lest we import some random version on sys.path.
version = get_version(_APP_FILE)

_dev_mode_: bool = True

if _dev_mode_:
    print('Running setup for {} version {}...'.format(_APP_FILE, version))
else:
    setup(
            name='appdirs',
            version=version,
            description='A small Python module for determining appropriate ' + \
                'platform-specific dirs, e.g. a "user data dir".',
            long_description=read('README.rst') + '\n' + read('CHANGES.rst'),
            python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
            classifiers=[
                'Development Status :: 5 - Production/Stable',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Programming Language :: Python :: 2',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.5',
                'Programming Language :: Python :: 3.6',
                'Programming Language :: Python :: 3.7',
                'Programming Language :: Python :: 3.8',
                'Programming Language :: Python :: Implementation :: PyPy',
                'Programming Language :: Python :: Implementation :: CPython',
                'Topic :: Software Development :: Libraries :: Python Modules',
            ],
            keywords='application directory log cache user',
            author='Trent Mick',
            author_email='trentm@gmail.com',
            maintainer='Trent Mick; Sridhar Ratnakumar; Jeff Rouse',
            maintainer_email='trentm@gmail.com; github@srid.name; jr@its.to',
            url='https://github.com/ActiveState/appdirs',
            license='MIT',
            py_modules=["appdirs"],
        )
