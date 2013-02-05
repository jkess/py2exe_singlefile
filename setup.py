#/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: James Kessler (<kessle10@gmail.com>)
#

"""Builds a single Windows executable from a Python script."""

import os
import sys
try:
    from distutils.core import setup
    import py2exe
except ImportError:
    sys.exit("Install distutils and py2exe")

# the python file to build into an exe
# if it's not set, use the first file with .py extension
PYEXEFILE = None  # filename.py

if not PYEXEFILE:
    thisdir = os.path.abspath(os.path.dirname(os.path.join(__file__)))
    for f in os.listdir(thisdir):
        name, ext = os.path.splitext(f)
        if ".py" in ext.lower() and name.lower() != "setup":
            PYEXEFILE = f
            break

if not PYEXEFILE:
    sys.exit("The python file must be in the same directory as setup.py")

# If run without args, build executables, in quiet mode.
if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

# pywin32 COM pulls in a lot of stuff which we don't want or need.
excludes = ["pywin", "pywin.debugger", "pywin.debugger.dbgcon",
            "pywin.dialogs", "pywin.dialogs.list", "win32com.server"]

options = {"bundle_files": 1,  # create singlefile exe
           "compressed": 1,  # compress the library archive
           "excludes": excludes,
           "dll_excludes": ["w9xpopen.exe", "mswsock.dll", "powrprof.dll"],
           }

setup(options={"py2exe": options},
      zipfile=None,  # append zip-archive to the executable.
      console=[PYEXEFILE]
      )
