from ursina import *
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

app = Ursina()
# camera.orthographic = True

camera.z = -50

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
                
def myclick(i,j):
    print("myclick", i,j)
    

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