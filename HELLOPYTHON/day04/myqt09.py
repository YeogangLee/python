import sys 
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from random import random

form_class = uic.loadUiType("./myqt09.ui")[0]

class WindowClass(QMainWindow, form_class): 
    
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb0.clicked.connect(self.myclick)
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb_call.clicked.connect(self.myclick)
        
    def myclick(self):
        # print(self, a)
        
        QMessageBox.question(self.window, 'Message', 'Calling...\n' + '', QMessageBox.Yes, QMessageBox.NoButton)      
        
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()
