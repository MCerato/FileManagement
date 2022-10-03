# -*- coding: utf-8 -*-
"""Manage the bank file.

Description
-----------
Object from wich you can manage the file you're using in your BankApp.
You can get the content and save a new content into it.

.. note::
    names and content of file are organised separately.

Libraries/Modules
-----------------
- time standard library (https://docs.python.org/3/library/time.html)
    - Access to sleep function.
- os standard library (https://docs.python.org/3/library/os.html)
    - Access to files function.
- Cfichier module (local)
    - Access to file methods.

Version
-------
- 1.0.0.0

TODO
----
- None.

Author(s)
---------
- Created by M. Cerato on 06/17/2022.
- Modified by xxx on xx/xx/xxxx.

Copyright (c) 2022 Cerato Workshop.  All rights reserved.

Members
-------
"""


# In[1]: imports
import sys
import os

# ************* Directories Setup ***************
absolutepath = os.path.abspath(__file__)
pkgDirectories = os.path.dirname(absolutepath)
while os.path.basename(pkgDirectories) != "FileManagement":
    pkgDirectories = os.path.dirname(pkgDirectories)

workingPath = os.path.join(pkgDirectories, "Sources/Packages/File")

if not workingPath in sys.path:
    sys.path.insert(0, workingPath)

# ***********************************************
import TXTFile

import time


    # In[1]: constructor & destructor
    
resumePath = "D:/temp_perso/FileManagement/Sources/Profile.txt"
NotTXTFilePath = "D:/temp_perso/FileManagement/Sources/plop.txt"
WriteFilePath = "D:/temp_perso/FileManagement/Tests/WritingTest.txt"

resumeTXT = TXTFile.TXT(resumePath) # create the object
print(resumeTXT)
print(resumeTXT.GetFileFormat())
resumeRawTXT = resumeTXT.GetAllContent()
resumeSplittedText = resumeTXT.GetLinesContent()
resumeLine = resumeTXT.GetLineContent(3)

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




randomFile = TXTFile.TXT(NotTXTFilePath) # Create An other PDF file object with a wrong link
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
