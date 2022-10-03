# -*- coding: utf-8 -*-
"""Manage the bank file.

Description
-----------
Object inherited from FileWrapper class and contning specific method to extract
Datas.   

Instead of FileWrapper, this Class has to be associated with a PDFFile

You can also get (read) the content and save a new content into it.

.. warning::
    You can't manipulate datas directly from/to the file.
    It is recommended to export the content of the file for treatment as
    a list of strings wich is easier to manipulate in python.


https://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/

Libraries/Modules
-----------------
- os standard library (https://docs.python.org/3/library/os.html)
    - Access to files function.

Version
-------
- 1.0.0.0

Notes
-----
- None.

TODO
----
- None.

Author(s)
---------
- Created by M. Cerato on 06/17/2022.
- Modified by xxx on xx/xx/xxxx.

Copyright (c) 2020 Cerato Workshop.  All rights reserved.

Members
-------
"""

# In[1]: imports
import sys
import os
import FileWrapper as fw

class TXT(fw.File):
    # In[1]: constructor & destructor

    """Class representing the file.
    
    :param path:
        where the file is.
        Path should be absolute with format ``C:/file1/file2/sourcefile``
    :type path:
        str
    :param name:
        Name of the file.
        Enter the name without extension
    :type name:
        str
    :param month:
        **Number** of the month (i.e 1 for January).
    :type month:
        int
    
    """

    def __init__(self, userPath):
        fw.File.__init__(self)

        self.CreateFile(userPath) # link the PDF to the object
        
        if self.GetFileFormat() != ".txt":
            print("wrong file format")
            print(f"This is a {self.GetFileFormat()}")
            print(f"")
        
    def __del__(self):
        """Destroying object.

        Mainly used to close file in case something went wrong
        """
        print(f"{self} deleted")

    def __repr__(self):
        """Display the object of the file."""

        return f"txt file : {self.GetFileName()}"


# In[3]: Content of the file
    def GetAllContent(self):
        """Return the entire file.

        :return:
            Return the entire content of the file as one big string
        :rtype:
            str

        .. note::
            displays the carriage return + line feed
        """
        if self.GetFileFormat() == ".txt":
            with open(os.path.join(self.GetFilePath(), self.GetFileName()),
                      mode='r', encoding="utf-8") as file:
                content = file.read()
            return content
        else:
            return None

    def GetLinesContent(self):
        """Return the entire file.

        :return:
            Return the entire content of the file as one big string
        :rtype:
            str

        .. note::
            displays the carriage return + line feed
        """
        if self.GetFileFormat() == ".txt":
            with open(os.path.join(self.GetFilePath(),
                                   self.GetFileName()),
                      mode='r' ,encoding="utf-8") as file:
                content = file.readlines()
            return content
        else:
            return None

    def GetLineContent(self, line):
        """Give the specific line of the file.

        :param line:
            Line to read.
        :type line:
            int
        :return:
            Return the line as a string
        :rtype:
            str

        .. note::
            displays the carriage return + line feed

        .. note::
            return an empty string if the line is out of bound or empty.
        """
        if self.GetFileFormat() == ".txt":
            if line > 0 and line <= len(self.GetLinesContent()):

                with open(os.path.join(self.GetFilePath(),
                                       self.GetFileName()), 
                          mode='r', encoding="utf-8") as file:
                    for i in range(line):
                        content = file.readline()
                return content
            else:
                print("line doesn't exist")
        else:
            return None

    def AddContent(self, contentToWrite):
        """Give the specific line of the file.

        :param line:
            Line to read.
        :type line:
            int
        :return:
            Return the line as a string
        :rtype:
            str

        .. note::
            displays the carriage return + line feed

        .. note::
            return an empty string if the line is out of bound or empty.
        """
        if self.GetFileFormat() == ".txt":
            with open(os.path.join(self.GetFilePath(),
                                   self.GetFileName()),
                      mode='a', encoding="utf-8") as file:
                if contentToWrite[len(contentToWrite)-1:] == "\n":
                    file.writelines(contentToWrite)
                else:
                    file.writelines(contentToWrite + "\n")

    def ReplaceContent(self, contentToWrite):
        """Give the specific line of the file.

        :param line:
            Line to read.
        :type line:
            int
        :return:
            Return the line as a string
        :rtype:
            str

        .. note::
            displays the carriage return + line feed

        .. note::
            return an empty string if the line is out of bound or empty.
        """
        if self.GetFileFormat() == ".txt":
            with open(os.path.join(self.GetFilePath(),
                                   self.GetFileName()),
                      mode='w', encoding="utf-8") as file:
                file.writelines(contentToWrite)

    def EraseContent(self):
        """Give the specific line of the file.

        :param line:
            Line to read.
        :type line:
            int
        :return:
            Return the line as a string
        :rtype:
            str

        .. note::
            displays the carriage return + line feed

        .. note::
            return an empty string if the line is out of bound or empty.
        """
        if self.GetFileFormat() == ".txt":
            with open(os.path.join(self.GetFilePath(),
                                   self.GetFileName()),
                      mode='w', encoding="utf-8") as file:
                file.writelines("")

# In[5]: internal functions for file content itself
    def __IsFileEmpty(self):
        """(local method) check if the file is empty.

        :return:
            Return ``True`` or ``False``
        :rtype:
            bool
        """
        if self.GetFileSize() != 0:
            isEmpty = False
        else:
            isEmpty = True
        return isEmpty

