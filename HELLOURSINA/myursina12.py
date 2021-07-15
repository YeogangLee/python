from ursina import *

app = Ursina()

# player = Entity(model='cube', color=color.orange)

camera.rotation_x = 90
camera.y = 40
camera.z = 0

pb2D = []
omok_size = [10]
orthographic = True 

for i in range(omok_size[0]) :
    for j in range(omok_size[0]) :
        temp = Entity(model='cube', texture='0', collider='box')
        temp.z = 4.5 - i
        temp.x = -4.5 + j
    
def update():
    # camera.rotation_y += held_keys['d']* 1
    # camera.rotation_y -= held_keys['a']* 1
    camera.rotation_y += .1
    

       
app.run()