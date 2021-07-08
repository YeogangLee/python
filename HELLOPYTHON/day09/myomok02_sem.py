import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.Qt import QPushButton, QSize
from PyQt5 import uic, QtWidgets
import numpy as np

form_class = uic.loadUiType("myomok02.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.omok_size = 19
        
        self.arr2D = [
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0]
            ]
        
        self.pb2D = []
        
        self.setupUi(self)
        self.create_pb()
        self.flag_wb = True
        self.flag_ing = True
        self.cntB = 0
        self.cntW = 0
        # self.cnt = 0
        self.pb_reset.clicked.connect(self.myreset)
        
        
    def myreset(self):
        self.flag_wb = True
        self.flag_ing = True

        # 배열에 들어가면 레퍼런스값이 된다, (일반 값이 아니라) 그래서 일일이 찍어준다.
        for i in range(self.omok_size) :
            for j in range(self.omok_size) :
                self.arr2D[i][j] = 0
        self.myrender()
        
        
    def myclick(self):
        # 비즈니스 로직을 제일 위에서 막는 것
        # if self.flag_ing == True :
        if not self.flag_ing :
            return 
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j] > 0 :
            return
        
        stone = -1
        
        if self.flag_wb :
            self.arr2D[i][j] = 1
            stone = 1
        else :
            self.arr2D[i][j] = 2
            stone = 2
        
        UP = self.getUP(i, j, stone)
        DW = self.getDW(i, j, stone)
        LE = self.getLE(i, j, stone)
        RI = self.getRI(i, j, stone)
        
        UL = self.getUL(i, j, stone)
        UR = self.getUR(i, j, stone)
        DL = self.getDL(i, j, stone)
        DR = self.getDR(i, j, stone)
        
        print("{} {} {}".format(UL,UP,UR))
        print("{} 1 {}".format(LE,RI))
        print("{} {} {}".format(DL,DW,DR))
        print("=")
        
        D1 = UP + DW + 1
        D2 = UR + DL + 1
        D3 = RI + LE + 1
        D4 = DR + UL + 1
        self.myrender()
        
        if D1 == 5 or D2 == 5 or D3 == 5 or D4 == 5 :
            if self.flag_wb :
                QtWidgets.QMessageBox.information(self, "Omok", "흰돌 승리")
            else :
                QtWidgets.QMessageBox.information(self, "Omok", "검은돌 승리")
            
            self.flag_ing = False
                

        self.flag_wb = not self.flag_wb
        
    
    def create_pb(self):
        for i in range(self.omok_size):
            line = []
            for j in range(self.omok_size):
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
        for i in range(self.omok_size):
            for j in range(self.omok_size):                    
                if self.arr2D[i][j] == 0 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                
                elif self.arr2D[i][j] == 1 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                
                elif self.arr2D[i][j] == 2 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))


    def getUP(self, i, j, stone):
        cnt = 0
        try : 
            while True :
                i -= 1
                if i < 0 : # i가 음수 인덱스를 읽어온다, 오목판은 끝과 끝이 이어져 있지 않다.
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt+=1
                else :
                    return cnt
        except :
            return cnt
            
    def getDW(self, i, j, stone):
        cnt = 0
        try : 
            while True :
                i += 1
                if i < 0 :
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt+=1
                else :
                    return cnt
        except :
            return cnt
        
    def getLE(self, i, j, stone):
        cnt = 0
        try : 
            while True :
                j -= 1
                if i < 0 : 
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt+=1
                else :
                    return cnt
        except :
            return cnt
        
    def getRI(self, i, j, stone):
        cnt = 0
        try : 
            while True :
                j += 1
                if i < 0 : 
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt+=1
                else :
                    return cnt
        except :
            return cnt
        
    def getUL(self, i, j, stone):
        cnt = 0
        try : 
            while True :
                i -= 1
                j -= 1
                if i < 0 : 
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt+=1
                else :
                    return cnt
        except :
            return cnt
        
    def getUR(self, i, j, stone):
        cnt = 0
        try : 
            while True :
                i -= 1
                j += 1
                if i < 0 : 
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt+=1
                else :
                    return cnt
        except :
            return cnt
        
    def getDL(self, i, j, stone):
        cnt = 0
        try : 
            while True :
                i += 1
                j -= 1
                if i < 0 : 
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt+=1
                else :
                    return cnt
        except :
            return cnt
        
    def getDR(self, i, j, stone):
        cnt = 0
        try : 
            while True :
                i += 1
                j += 1
                if i < 0 : 
                    return cnt
                if j < 0 : 
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt+=1
                else :
                    return cnt
        except :
            return cnt
        
        
if __name__ == "__main__" :

    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()