# -*- coding: utf-8 -*-
"""Test the class FileWrapper.

Description
-----------
Sequence of tests for FileWrapper methods.

.. warning::
    Test non exhaustive (WIP - learning on tests methods)

.. note::
    add waiting time when files are created

Libraries/Modules
-----------------
- sys standard library (https://docs.python.org/3/library/sys.html)
    - Access to functions interacting with interpreter.
- os standard library (https://docs.python.org/3/library/os.html)
    - Access to files function.
- time standard library (https://docs.python.org/2/library/time.html)
    - Access to time-related functions.
- PDFFile library (:file:FileWrapper.html)
    - Access to files functions.

Version
-------
- 1.0.0.0

Notes
-----
- None

TODO
----
- Implement Tests according to Official tests protocol

Author(s)
---------
- Created by M. Cerato on 10/05/2022.
- Modified by xxx on xx/xx/xxxx.

Copyright (c) 2022 Cerato Workshop.  All rights reserved.

Members
-------
"""

# In[1]: imports
import sys
import os

import time

# ************* Directories Setup ***************
projectName = "FileManagement"
absolutepath = os.path.abspath(__file__)
pkgDirectories = os.path.dirname(absolutepath)
while os.path.basename(pkgDirectories) != projectName:
    pkgDirectories = os.path.dirname(pkgDirectories)

workingPath = os.path.join(pkgDirectories, "Sources/Packages/File")

if workingPath not in sys.path:
    sys.path.insert(0, workingPath)

# ***********************************************
import FileWrapper as fw

# In[1]: constructor & destructor
existingPath = "D:/temp_perso/FileManagement/Sources/Profile.pdf"
# existingPath = os.path.abspath(existingPath)
# existingPath = existingPath.replace("\\", "/")

nonExistingPath = "D:/temp_perso/FileManagement/Sources/plopi.pdf"
# nonExistingPath = os.path.abspath(nonExistingPath)
# nonExistingPath = nonExistingPath.replace("\\", "/")

f1 = fw.File()
f2 = fw.File()
print(f"f1 : {f1}")
print(f"f2 : {f2} \n")

print(f2.GetFileSize())
print(f2.GetFileFormat())


f1.CreateFile(nonExistingPath)
f2.SelectFile(existingPath)
print(f"f1 : {f1}")
print(f"f2 : {f2} \n")

print(f"f2 size : {f2.GetFileSize()}")
print(f"f2 ext : {f2.GetFileFormat()}\n")

print(f"f1 size : {f1.GetFileSize()}")
print(f"f1 ext : {f1.GetFileFormat()}\n")

time.sleep(2)
f1.RenameFile("plop.txt")
time.sleep(2)
f1.MoveFile("D:/temp_perso/FileManagement/Sources/API")
time.sleep(2)
f1.MoveFile("D:/temp_perso/FileManagement/Sources")
time.sleep(2)
f1.DeleteFile()
print(f1)

del f1
del f2
