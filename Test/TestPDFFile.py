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

workingPath = os.path.join(pkgDirectories, "FileManagementSources/Packages/File")

if not workingPath in sys.path:
    sys.path.insert(0, workingPath)

# ***********************************************
import PDFFile

import time


    # In[1]: constructor & destructor
    
resumePath = "D:/temp_perso/FileManagement/FileManagementSources/Profile.pdf"
NotPDFFilePath = "D:/temp_perso/FileManagement/FileManagementSources/plop.pdf"

resumePDF = PDFFile.PDF(resumePath) # create the object

print(resumePDF.GetFileFormat())
resumeText = resumePDF.GetAllContent()
resumeSplittedText = resumePDF.GetLinesContent()
resumeLine = resumePDF.GetLineContent(3)

randomFile = PDFFile.PDF(NotPDFFilePath) # Create An other PDF file object with a wrong link
time.sleep(2)
randomFile.DeleteFile()


del resumePDF
del randomFile
