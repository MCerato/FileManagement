# -*- coding: utf-8 -*-
"""Test the class TXT from TXTFile.

Description
-----------
Sequence of tests for TXTFIle methods.

.. warning::
    Tests non exhaustive (WIP - learning on tests methods)

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
- PDFFile library (:file:TXTFile.html)
    - Access to PDF files function.

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
import TXTFile

# In[1]: constructor & destructor

resumePath = "D:/temp_perso/FileManagement/Sources/Profile.txt"
NotTXTFilePath = "D:/temp_perso/FileManagement/Sources/plop.txt"
WriteFilePath = "D:/temp_perso/FileManagement/Tests/WritingTest.txt"

resumeTXT = TXTFile.TXT(resumePath)  # create the object
print(resumeTXT)
print(resumeTXT.GetFileFormat())
resumeRawTXT = resumeTXT.GetAllContent()
resumeSplittedText = resumeTXT.GetLinesContent()
resumeLine = resumeTXT.GetLineContent(3)
print(resumeLine)

writingTXT = TXTFile.TXT(WriteFilePath)
print(writingTXT)
print(writingTXT.GetFileFormat())
print("")

writingTXT.AddContent(resumeLine)
time.sleep(2)
writingTXT.AddContent(resumeLine)
time.sleep(2)
writingTXT.ReplaceContent(resumeSplittedText)
time.sleep(2)
writingTXT.EraseContent()

# Create An other PDF file object with a wrong link
randomFile = TXTFile.TXT(NotTXTFilePath)
print(resumeTXT)
time.sleep(2)
randomFile.RenameFile("yo.txt")
time.sleep(2)
randomFile.MoveFile("D:/temp_perso/FileManagement/Sources/API")
time.sleep(2)
randomFile.MoveFile("D:/temp_perso/FileManagement/Sources")
time.sleep(2)
randomFile.DeleteFile()


del resumeTXT
del randomFile
del writingTXT
