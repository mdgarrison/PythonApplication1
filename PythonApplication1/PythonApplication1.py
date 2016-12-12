import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal

Ui_MainWindow, QtBaseClass = uic.loadUiType("MainWindow.ui")

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Here's an example of connecting a widget to Python code; in this case,
        # the clicked status of a QButton is connected to a Python method
        self.ui.pushButton1.clicked.connect(self.HandlePushButton1Clicked)
        self.ui.pushButton2.clicked.connect(self.HandlePushButton2Clicked)

        # Here's an example of connecting 2 widgets without any intervening code;
        # in this case, the value of a QLcdNumber widget is connected to the
        # value of a QDial
        self.ui.dial1.valueChanged.connect(self.ui.lcdNumber1.display)
        self.ui.horizontalSlider1.valueChanged.connect(self.ui.lcdNumber2.display)
        self.ui.dial1.valueChanged.connect(self.ui.progressBar1.setValue)

        # Here's another example of connecting 2 widgets outside of the code; in
        # case, a little more unusual connection between the values of the two
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.connect_trigger()
    window.show()
    sys.exit(app.exec_())
