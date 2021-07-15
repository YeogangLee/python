from ursina import *

app = Ursina()

def myreset():
    print("myreset")
    btn.visible = False
    
btn = Button(text='RESET', origin=(-4,-5.5), scale=(0.11, 0.07, 1), background=True, on_click=myreset)

def update():
    camera.rotation_z += held_keys['d']* 1
    camera.rotation_z -= held_keys['a']* 1
       
app.run()