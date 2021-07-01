import sys 
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./myqt05.ui")[0]

class WindowClass(QMainWindow, form_class): 
    
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.sum)
        
    def sum(self):
        le1Txt = int(self.le1.text())
        le2Txt = int(self.le2.text())
        
        result = 0
        for i in range(le1Txt, le2Txt+1):
            result += i
            i+=1
        
        self.le3.setText(str(result))
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()
