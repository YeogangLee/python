import sys 
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("./myqt07.ui")[0]

class WindowClass(QMainWindow, form_class): 
    
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myenter)
    
    def myenter(self):
        # print("myenter")
        self.doGame()
        
    def myclick(self):
        self.doGame()
        
    def doGame(self):
         
        rnd = random()
        
        if(rnd > 0.5):
            self.le_com.setText("홀") 
        else:
            self.le_com.setText("짝")
                
        if(self.le_mine.text() == self.le_com.text()):
            self.le_result.setText("승리하셨습니다!") 
        else:
            self.le_result.setText("패배하셨습니다...")
            
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()
