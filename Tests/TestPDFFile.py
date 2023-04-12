# -*- coding: utf-8 -*-
"""Test the class PDF from PDFFile.

Description
-----------
Sequence of tests for PDFFIle methods.

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
- PDFFile library (:file:PDFFile.html)
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
import PDFFile

# In[1]: constructor & destructor

resumePath = "D:/temp_perso/FileManagement/Sources/Profile.pdf"
NotPDFFilePath = "D:/temp_perso/FileManagement/Sources/plop.pdf"

resumePDF = PDFFile.PDF(resumePath)  # create the object
metaDataz = resumePDF.GetMetaPDF()

resumeText = resumePDF.GetAllContent()
resumeSplittedText = resumePDF.GetLinesContent()
resumeLine = resumePDF.GetLineContent(3)

# Create An other PDF file object with a wrong link
randomFile = PDFFile.PDF(NotPDFFilePath)
time.sleep(2)
randomFile.DeleteFile()

del resumePDF
del randomFile
