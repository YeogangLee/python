# -*- coding: utf-8 -*-
from ursina import *
from IPython.utils import encoding
Text.default_font = "/c/Windows/Fonts/gulim.ttc"
# 참고 : https://www.youtube.com/watch?v=DetFRfJ3xI8

arr2D = [
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0]
            ]

pb2D = []
flag_wb = [True]
flag_ing = [True]
omok_size = [10]

app = Ursina()
# camera.orthographic = True

camera.z = -50

def myreset():
    print("myreset")
    btn.visible = False
    btn_v.visible = False
    btn_v.enabled = False
    
    flag_wb[0] = True
    flag_ing[0] = True

    # 배열에 들어가면 레퍼런스값이 된다, (일반 값이 아니라) 그래서 일일이 찍어준다.
    for i in range(omok_size[0]) :
        for j in range(omok_size[0]) :
            arr2D[i][j] = 0
    myrender()
    

def myclose():
    print("myclose")
    btn_v.visible = False
    btn_v.enabled = False

    
btn = Button(text='RESET', origin=(-4,-5.5), scale=(0.11, 0.07, 1), background=True, on_click=myreset)
btn_v = Button(text='**승리', origin=(0,0), scale=(0.11, 0.07, 1), background=True, enabled=False, on_click=myclose, visible=False)
btn_v.z = -25

def myrender():
    for i in range(10) :
        for j in range(10) :
            if arr2D[i][j] == 0 :
                pb2D[i][j].z = 0.7
                pb2D[i][j].color = color.white
            
            elif arr2D[i][j] == 1 :
                pb2D[i][j].z = -0.7
                pb2D[i][j].color = color.white
                                 
            elif arr2D[i][j] == 2 :
                pb2D[i][j].z = -0.7
                pb2D[i][j].color = color.black
                
def getUP(i, j, stone):
    cnt = 0
    try : 
        while True :
            i -= 1
            if i < 0 :
                return cnt
            if j < 0 : 
                return cnt
            if arr2D[i][j] == stone :
                cnt+=1
            else :
                return cnt
    except :
        return cnt
    
def getDW(i, j, stone):
        cnt = 0
        try : 
            while True :
                i += 1
                if i < 0 :
                    return cnt
                if j < 0 : 
                    return cnt
                if arr2D[i][j] == stone :
                    cnt+=1
                else :
                    return cnt
        except :
            return cnt
        
def getLE(i, j, stone):
    cnt = 0
    try : 
        while True :
            j -= 1
            if i < 0 : 
                return cnt
            if j < 0 : 
                return cnt
            if arr2D[i][j] == stone :
                cnt+=1
            else :
                return cnt
    except :
        return cnt
    
def getRI(i, j, stone):
    cnt = 0
    try : 
        while True :
            j += 1
            if i < 0 : 
                return cnt
            if j < 0 : 
                return cnt
            if arr2D[i][j] == stone :
                cnt+=1
            else :
                return cnt
    except :
        return cnt
    
def getUL(i, j, stone):
    cnt = 0
    try : 
        while True :
            i -= 1
            j -= 1
            if i < 0 : 
                return cnt
            if j < 0 : 
                return cnt
            if arr2D[i][j] == stone :
                cnt+=1
            else :
                return cnt
    except :
        return cnt
    
def getUR(i, j, stone):
    cnt = 0
    try : 
        while True :
            i -= 1
            j += 1
            if i < 0 : 
                return cnt
            if j < 0 : 
                return cnt
            if arr2D[i][j] == stone :
                cnt+=1
            else :
                return cnt
    except :
        return cnt
    
def getDL(i, j, stone):
    cnt = 0
    try : 
        while True :
            i += 1
            j -= 1
            if i < 0 : 
                return cnt
            if j < 0 : 
                return cnt
            if arr2D[i][j] == stone :
                cnt+=1
            else :
                return cnt
    except :
        return cnt
    
def getDR(i, j, stone):
    cnt = 0
    try : 
        while True :
            i += 1
            j += 1
            if i < 0 : 
                return cnt
            if j < 0 : 
                return cnt
            if arr2D[i][j] == stone :
                cnt+=1
            else :
                return cnt
    except :
        return cnt
                
def myclick(i,j):
    if not flag_ing[0] :
        return
    
    if arr2D[i][j] > 0 :
        return
        
    stone = -1
    if flag_wb[0] :
        arr2D[i][j] = 1
        stone = 1
    else :
        arr2D[i][j] = 2
        stone = 2
        
    up = getUP(i, j, stone)
    dw = getDW(i, j, stone)
    le = getLE(i, j, stone)
    ri = getRI(i, j, stone)
    
    ul = getUL(i, j, stone)
    ur = getUR(i, j, stone)
    dl = getDL(i, j, stone)
    dr = getDR(i, j, stone)
        
    print("{} {} {}".format(ul,up,ur))
    print("{} 1 {}".format(le,ri))
    print("{} {} {}".format(dl,dw,dr))
    print("========")
    
    D1 = up + dw + 1
    D2 = ur + dl + 1
    D3 = ri + le + 1
    D4 = dr + ul + 1
    
    myrender()
    
    if D1 == 5 or D2 == 5 or D3 == 5 or D4 == 5 :
        if flag_wb[0] :
            # b = Button('흰돌 승리', color=color.azure, scale=.14, text_origin=(0,0))
            # b.z = 1
            btn_v.text = '흰돌 승리'
            btn_v.visible = True
            btn_v.z = 5
            btn_v.enabled = True
            
        else :
            # b = Button('흑돌 승리', color=color.azure, scale=.14, text_origin=(0,0))
            # b.z = 1
            btn_v.text = '흑돌 승리'
            btn_v.visible = True
            btn_v.z = 5
            btn_v.enabled = True
        
        flag_ing[0] = not flag_ing[0]

    
    flag_wb[0] = not flag_wb[0]

for i in range(10) :
    line = []
    for j in range(10) :
        pb = Entity(model='cube', texture='0', collider='box', on_click=Func(myclick,i,j))
        pb.x = j - 4.5
        pb.y = - i + 4.5
        
        sp = Entity(model='sphere', color=color.black, scale=(0.8,0.8,0.3))
        sp.x = j - 4.5
        sp.y = - i + 4.5
        sp.z = 1
        line.append(sp)
    pb2D.append(line)



def update():
    camera.z += held_keys['d']* .1
    camera.z -= held_keys['a']* .1
        
    
       
app.run()