import sys 
from PyQt5 import uic, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import time, threading

form_class = uic.loadUiType("./myqt_messenger_thread_o.ui")[0]

class WindowClass(QMainWindow, form_class): 
    
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        # self.le.returnPressed.connect(self.myclick)
                
    def myfunc_th(self):
        print("myfunc_th")
        # for i in range(5):
        #     time.sleep(1)
        #     a = self.lbl.text()
        #     int_a = int(a)
        #     int_a += 1
        #     self.lbl.setText(str(int_a)) 
        

    def myclick(self):
        # my_t1 = threading.Thread(target=self.myfunc_th)
        # my_t1.start()

        print("myfunc_th")
        for i in range(5):
            time.sleep(1)
            a = self.lbl.text()
            int_a = int(a)
            int_a += 1
            self.lbl.setText(str(int_a)) 
        
        
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()
