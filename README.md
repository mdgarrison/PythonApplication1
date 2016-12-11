This is a Python project hosted in Visual Studio 2015, using "Python Tools for Visual Studio" along with Python 3.5.2 and PyQt5.

Qt Designer v5.7.0 was used to create the .ui file; this gives us the visual layout of the window.

The underlying Python code is where all of the logic resides (i.e., I didn't connect any widgets in the .ui file).

There are 2 ways of processing a Qt .ui file:

1. Run it under the Pyuic5 command-line utility to spit out a Python module that you can use in your main code; and
2. Load the .ui file from your main code.

This project uses approach (2).

Environment Set-up (Windows):

Step 1: Download and install Qt Open Source (https://www.qt.io/download/)

Step 2: Download and install Microsoft Visual Studio 2015 Community (https://www.visualstudio.com/downloads/)

Step 3: Download and install Python Tools for Visual Studio (https://microsoft.github.io/PTVS)

Step 4: Download and install Python v3.5.2 (https://www.python.org)

Step 5: Use the Python 'pip' utility to install PyQt5 ("python -m pip install PyQt5")

Step 6: Confirm successful setup by running Python in a command window and typing the following at the ">>>" prompt:

>>> import PyQt5.QtCore
>>> import PyQt5.QtGui
>>> import PyQt5.QtWidgets

If no errors were displayed, your PyQt5 library is correctly set up, and should show up in the package listing in
Visual Studio.
