import sys 
from PyQt5 import uic, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./myqt_messenger.ui")[0]

class WindowClass(QMainWindow, form_class): 
    
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le.returnPressed.connect(self.myclick)
        
    def myclick(self):
        str_old = self.te.toPlainText()
        str_new = self.le.text()
        txt = str_old + "\n" + str_new

        self.te.setPlainText(txt)
        self.le.setText("")
        self.te.moveCursor(QtGui.QTextCursor.End)
        
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()
