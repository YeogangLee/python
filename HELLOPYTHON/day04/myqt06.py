import sys 
from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./myqt06.ui")[0]

class WindowClass(QMainWindow, form_class): 
    
    def __init__(self): 
        super().__init__() 
        self.setupUi(self)
        self.pb.clicked.connect(self.sum)
        
    def sum(self):
        # 여기서 int()로 형변환을 안 하면, 아래에서 찍어줄 때 할 작업이 적어진다.
        # 다음에는 그렇게...
        # 아니, format()을 사용하면 여기서 int()로 형변환이 유리하다.
        le1Txt = int(self.le1.text())
        
        result = ""
        result += str(le1Txt) + " x 1 = " + str(le1Txt * 1)  + "\n"
        result += str(le1Txt) + " x 2 = " + str(le1Txt * 2)  + "\n"
        result += str(le1Txt) + " x 3 = " + str(le1Txt * 3)  + "\n"
        result += str(le1Txt) + " x 4 = " + str(le1Txt * 4)  + "\n"
        result += str(le1Txt) + " x 5 = " + str(le1Txt * 5)  + "\n"
        result += str(le1Txt) + " x 6 = " + str(le1Txt * 6)  + "\n"
        result += str(le1Txt) + " x 7 = " + str(le1Txt * 7)  + "\n"
        result += str(le1Txt) + " x 8 = " + str(le1Txt * 8)  + "\n"
        result += str(le1Txt) + " x 9 = " + str(le1Txt * 9)  + "\n"
        
        # format() 함수 사용
        # result += "{} x {} = {}\n".format(le1Txt,1,le1Txt*1)
        
        # for문을 사용하더라도, 구구단의 잔재를 최대한 남길 수 있도록 10이 아닌, 9+1
        # for i in range(1, 9+1):
        
        self.te.setText(result)
        
if __name__ == "__main__": 
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()
