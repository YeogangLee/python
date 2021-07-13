from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange, scale_y=2)

def update():
    camera.rotation_z += held_keys['d']* 1
    camera.rotation_z -= held_keys['a']* 1
    

def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y-1, delay=.25)
    
       
app.run()