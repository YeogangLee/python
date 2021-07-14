from ursina import *

app = Ursina()

def myclick():
    print("myclick")
    
# player = Entity(model='sphere', color=color.orange, scale=(1,1,1), position=(1,2,0))

player = Entity(model='sphere', color=color.white, scale=(1,0.3,1))

b = Button(text='hello world!', color=color.azure, icon='0', scale=.25, text_origin=(-.5,0))
b.on_click = myclick
b.tooltip = Tooltip('exit')



def update():
    camera.z += held_keys['d']* .1
    camera.z -= held_keys['a']* .1
    
    
    
    
       
app.run()