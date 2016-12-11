This is a Python project hosted in Visual Studio 2015, using "Python Tools for Visual Studio" along with Python 3.5.2 and PyQt5.

Qt Designer v5.7.0 was used to create the .ui file; this gives us the visual layout of the window.

The underlying Python code is where all of the logic resides (i.e., I didn't connect any widgets in the .ui file).

There are 2 ways of processing a Qt .ui file:

1. Run it under the Pyuic5 command-line utility to spit out a Python module that you can use in your main code; and
2. Load the .ui file from your main code.

This project uses approach (2).


