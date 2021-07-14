from ursina import *

app = Ursina()
# camera.orthographic = True
camera.z = -50

# stone = Entity(model='sphere', color=color.white, scale=(1,0.3,1))

def myclick(i,j):
    print("myclick", i,j)
    sp = Entity(model='sphere', texture='1', scale=(0.8,0.8,0.3))
    sp.x = j - 4.5
    sp.y = - i + 4.5
    sp.z = -1.5

D = 1

for i in range(10) :
    for j in range(10) :
        pb = Entity(model='cube', texture='0', collider='box', on_click=Func(myclick,i,j))
        pb.x = j - 4.5
        pb.y = - i + 4.5




def update():
    camera.rotation_x += held_keys['d']* .1
    camera.rotation_x -= held_keys['a']* .1
    
    
    
    
       
app.run()