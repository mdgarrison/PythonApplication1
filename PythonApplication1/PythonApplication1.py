import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

# This is pretty standard stuff for being able to load a .ui file
Ui_MainWindow, QtBaseClass = uic.loadUiType("MainWindow.ui")

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        # Here's more of the plumbing required to load a .ui file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Here's an example of connecting 2 widgets without any intervening code;
        # in this case, the value of a QLcdNumber widget is connected to the
        # value of a QDial
        self.ui.dial1.valueChanged.connect(self.ui.lcdNumber1.display)
        self.ui.horizontalSlider1.valueChanged.connect(self.ui.lcdNumber2.display)
        self.ui.dial1.valueChanged.connect(self.ui.progressBar1.setValue)
        # Get in the habit of reading it like this:
        # CONNECT FROM(dial1.valueChanged) TO(progressBar1.setValue)
        #     The object we call connect() on is the sender
        #     The object we pass in as the parameter is the receiver

        # Here's an example of connecting a widget to Python code; in this case,
        # the clicked status of a QButton is connected to a Python method
        self.ui.pushButton1.clicked.connect(self.HandlePushButton1Clicked)
        self.ui.pushButton2.clicked.connect(self.HandlePushButton2Clicked)

        # Here's another example of connecting 2 widgets outside of the code; in
        # this case, a little more unusual connection between the values of the two
        # sliders
        self.ui.horizontalSlider1.valueChanged.connect(self.ui.verticalSlider1.setValue)

    # This section of code shows an example of how to create a signal, how to connect it,
    # and how to emit it

    trigger = pyqtSignal()

    def connect_trigger(self):
        self.trigger.connect(self.handle_trigger)

    def handle_trigger(self):
        print("trigger signal received")

    def HandlePushButton1Clicked(self):
        self.ui.textEdit1.setText("Hello")
        self.trigger.emit()

    def HandlePushButton2Clicked(self):
        self.ui.textEdit1.setText("World")
        self.trigger.emit()

    # Here is an example of a function defined using type annotations (PEP 484)
    def greeting(name: str) -> str:
        return 'Hello ' + name

if __name__ == "__main__":
    # More generic plumbing -- this is how our app starts up
    app = QApplication(sys.argv)
    window = MyApp()

    # A non-standard addition -- here is where I connect the trigger
    window.connect_trigger()

    # Back to generic stuff
    window.show()
    sys.exit(app.exec_())
