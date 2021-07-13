from ursina import *

app = Ursina()

# player = Entity(model='sphere', color=color.orange, scale=(1,1,1), position=(1,2,0))

player = Entity(model='sphere', color=color.white, scale=(1,0.3,1))


def update():
    camera.z += held_keys['d']* .1
    camera.z -= held_keys['a']* .1
    
    
    
    
       
app.run()