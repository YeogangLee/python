import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.Qt import QPushButton

form_class = uic.loadUiType("myomok01.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.idx = 0
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        self.idx += 1
        namuji = self.idx % 3
        self.pb.setIcon(QtGui.QIcon('{}.png'.format(namuji)))
                

if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()