# -*- coding: utf-8 -*-


# In[1]: imports
import sys
import os

import time

# ************* Package Directory Setup ***************
absolutepath = os.path.abspath(__file__)
pkgDirectories = os.path.dirname(absolutepath)
while os.path.basename(pkgDirectories) != "FileManagement":
    pkgDirectories = os.path.dirname(pkgDirectories)
    print(pkgDirectories)

workingPath = os.path.join(pkgDirectories, "FileManagementSources/Packages/File")

if not workingPath in sys.path:
    sys.path.insert(0, workingPath)

# *****************************************************
import FileWrapper

    # In[1]: constructor & destructor
existingPath = "D:/temp_perso/FileManagement/FileManagementSources/Profile.pdf"
# existingPath = os.path.abspath(existingPath)
# existingPath = existingPath.replace("\\", "/")

nonExistingPath = "D:/temp_perso/FileManagement/FileManagementSources/plopi.pdf"
# nonExistingPath = os.path.abspath(nonExistingPath)
# nonExistingPath = nonExistingPath.replace("\\", "/")

f1 = FileWrapper.File()
f2 = FileWrapper.File()
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
f1.DeleteFile()
print(f1)

del f1
del f2
