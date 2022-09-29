FileManagement UserGuide (WIP)
==============================

WELCOME HERE! This documentation intend to show you how to use the package 
FileManagement

Description
-----------

FileManagement is a wrapper (simplifier) to manipulate specific files format
such as ``.pdf``, ``.txt``, ``.csv`` wich are the most used to common manipulations

Natively in this package, ``FileWrapper`` is better used with one of the file
format it has been created for. But If you feel it can be exploited for other 
file format, feel free to use it for personal purpose. 

Software Architecture
---------------------

How FileManagement has been designed is represented by the software architecture below:

.. image:: ../Diagram_UML.PNG

How To select the PBR
---------------------

It exists 2 type of connections to a Powerbrick. You can connect through the "maintenance port".
This ethernet port exists on every PowerBrick and always has the same adress.

The other way allows you to enter an IP adress manually.

.. attention:: Be careful on wich you are able to connect or not.
	The software doesn't check what device is on the network. He is pretty simple.

=========================== ================================
IP Adress Type              Description                     
=========================== ================================
Default IP Adress           Maintenance Adress 172.168.0.200
Custom IP adress            any Standard PBR adress
=========================== ================================

How To Download
---------------

The Download feature allows you to extract setups (in folders form or in files form) of a Power Birck. 
You'll have to select what setup you want to download. It goes from "usrflash" for the most recent parameters
to "usrflash.5" for the oldest.

.. note:: Choosing a path to download is not implemented yet. The files downloaded are put where the script is run.

You can then, press on the green button *"Download"*.

How To Upload
---------------

.. The second feature is the upload. If you need to send data to a Power Brick, it's the convenient feature.

.. Secondly, move on the blue button  "Upload" just below the Download button. Select, the remote directory where you'll 
.. send the data (folder or files).
.. Thirdly, you must enter the path (absolute path) to the folder you want to send.

.. Finally, press on the button "Upload" and look at log on your request in the display below.  

.. note::There is always a message in a pop up that shows you what is required to perform each task in PBR_OSMOS GUI.

.. caution:: Because of a bug, the dynamic update of the GUI does'nt work. So you need to press on buttons
	to get the entry fields (ip address Entry) enabled.
