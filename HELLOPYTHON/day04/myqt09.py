import sys 
from PyQt5 import uic, QtWidgets 
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
        self.pb_call.clicked.connect(self.mycall)
        
    def myclick(self):
        # print("hello")

        # print(self) 
        # 뭔가를 주고 있는데 뭔지를 모르겠어
        # 자바에서 들고올 때 뭘 들고왔죠? 
        # -> 자바의 e.getSource(), 이런게 pyqt에도 있다는 것 
        # 10번 말하기 : 소스 타겟 센더
        # 조금만 외워두면 로직이 훨씬 쉬워질 수 있어요~
        
        # print(self.sender())
        # print(self.sender().text()) # <=== 이거다!
        
        # print(self.source())
        # print(self.target())
        print(self.sender())
               
                
        str_old = self.le.text()
        str_new = self.sender().text()
        self.le.setText(str_old + str_new)
    
    def mycall(self):
        QtWidgets.QMessageBox.information(self, "Telephone", "calling...\n\n" + self.le.text())
        
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()
