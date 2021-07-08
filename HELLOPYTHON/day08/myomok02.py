import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.Qt import QPushButton, QSize

form_class = uic.loadUiType("myomok02.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        
        self.arr2D = [
                [0,0,0,0,0, 0,0,0,0,0],
                [0,1,2,0,0, 0,0,0,0,0],
                [0,0,1,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0]
            ]
        
        self.pb2D = []
        
        self.setupUi(self)
        self.create_pb()
        self.idx = 0
        
        
    def myclick(self):
        # print(self.sender().toolTip())
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        # print(arr_ij)
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        self.idx += 1
        
        if self.arr2D[i][j] == 0 :
            if self.idx % 2 == 1 :
                self.arr2D[i][j] = 1
            elif self.idx % 2 == 0 :
                self.arr2D[i][j] = 2
        
        self.myrender()
        
        
    
    def create_pb(self):
        for i in range(10):
            line = []
            for j in range(10):
                pb1 = QPushButton(self)
                pb1.setText('')
                # pb1.toolTip()
                pb1.setToolTip("{},{}".format(i,j))
                pb1.setIconSize(QSize(40,40))
                pb1.setGeometry(j*40, i*40, 40, 40)
                pb1.setIcon(QtGui.QIcon('0.png'))
                pb1.clicked.connect(self.myclick)
                line.append(pb1)
            self.pb2D.append(line)
        self.myrender()
            
            
    def myrender(self):
        for i in range(10):
            for j in range(10):                    
                if self.arr2D[i][j] == 0 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                
                elif self.arr2D[i][j] == 1 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                
                elif self.arr2D[i][j] == 2 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))

                    
        
if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()