from ursina import *

app = Ursina()
# camera.orthographic = True
camera.z = -50

def myclick(i,j):
    print("myclick", i,j)

D = 1

# pb1 = Entity(model='cube', texture='0', collider='box', on_click=Func(myclick,"0,0"))
# pb2 = Entity(model='cube', texture='0', collider='box', on_click=Func(myclick,"0,0"))
# pb1.x = 0
# pb2.x = 1


# entity_list = [None] * 10
# player_list = []

# for i in range(10) :
#     entity_list[i] = Entity(model='cube', texture='0', collider='box', on_click=Func(myclick,"0,0"))

for i in range(10) :
    for j in range(10) :
        pb = Entity(model='cube', texture='0', collider='box', on_click=Func(myclick,i,j))
        pb.x = j - 4.5
        pb.y = - i + 4.5 # y���� �� ������ + �̱� ������, i�� ������ ����, �򰥸��� i�� ����� ��������. ������ ������ �� �Ŵ�.

def update():
    camera.rotation_z += held_keys['d']* .1
    camera.rotation_z -= held_keys['a']* .1
    
    
    
    
       
app.run()