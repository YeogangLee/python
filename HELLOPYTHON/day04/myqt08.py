import sys 
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("./myqt08.ui")[0]

class WindowClass(QMainWindow, form_class): 
    
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myenter)
        
    def myclick(self):
        self.doGame()
        
    def myenter(self):
        self.doGame()
        
    def doGame(self):
        rnd = random()
        
        if(rnd > 0.66):
            self.le_com.setText("가위")
        elif(rnd > 0.33):
            self.le_com.setText("바위")
        else:
            self.le_com.setText("보")
                
        if(self.le_mine.text() == self.le_com.text()):
            self.le_result.setText("== 무승부 ==") 
        elif(self.le_mine.text() == "가위" and self.le_com.text() == "보" or self.le_mine.text() == "바위" and self.le_com.text() == "가위" or self.le_mine.text() == "보" and self.le_com.text() == "바위"):
            self.le_result.setText("승리하셨습니다!") 
        elif(self.le_mine.text() == "보" and self.le_com.text() == "가위" or self.le_mine.text() == "가위" and self.le_com.text() == "바위" or self.le_mine.text() == "바위" and self.le_com.text() == "보"):
            self.le_result.setText("패배하셨습니다...")
        
    
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()
