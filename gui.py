import sys
from PyQt5 import QtWidgets
from design import design

class ChatWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_handlers()

    def init_handlers(self):
        if self.pushButton.clicked.connect(self.send_message)

    def send_message(self):
        message = self.lineEdit.text()


app = QtWidgets.QApplication(sys.argv)