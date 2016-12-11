import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

Ui_MainWindow, QtBaseClass = uic.loadUiType("MainWindow.ui")

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton1.clicked.connect(self.HandlePushButton1Clicked)
        self.ui.pushButton2.clicked.connect(self.HandlePushButton2Clicked)

    def HandlePushButton1Clicked(self):
        self.ui.textEdit1.setText("Hello")

    def HandlePushButton2Clicked(self):
        self.ui.textEdit1.setText("World")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
