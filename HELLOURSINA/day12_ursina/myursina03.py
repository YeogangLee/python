from ursina import *

app = Ursina()

D = 5

# player = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(1,2,0))

player1 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(-D,D,0))
player2 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(0,D,0))
player3 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(D,D,0))

player4 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(-D,0,0))
player5 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(0,0,0))
player6 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(D,0,0))

player7 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(-D,-D,0))
player8 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(0,-D,0))
player9 = Entity(model='cube', color=color.orange, scale=(1,1,1), position=(D,-D,0))

camera.z = -30

def update():
    camera.z += held_keys['d']* .1
    camera.z -= held_keys['a']* .1
    
       
app.run()