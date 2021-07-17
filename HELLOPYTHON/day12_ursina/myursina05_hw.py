from ursina import *
import win32api
import time
from pynput.mouse import Button, Controller

app = Ursina()
mouse = Controller()

# player = Entity(model='sphere', color=color.orange, scale=(1,1,1), position=(1,2,0))

D = 3

player4 = Entity(model='sphere', color=color.white, scale=(1,0.3,1), position=(-D,0,0))
player5 = Entity(model='sphere', color=color.white, scale=(1,0.3,1), position=(0,0,0))
player6 = Entity(model='sphere', color=color.white, scale=(1,0.3,1), position=(D,0,0))

# camera.z = -30
# camera.y = 2

def update():
    camera.rotation_x += held_keys['d']* .1
    camera.rotation_x -= held_keys['a']* .1

# def ac():
#     if keystate < 0:
#         mouse.click(Button.left, 1)
#         time.sleep(0.1)
#     else:
#         pass
#
# while True:
#     keystate = win32api.GetAsyncKeyState(0x06)
#     ac()
       
       
input_handler.bind('s', 'arrow down')  # 's'-key will now be registered as 'arrow down'-key

def test():
    print('----')
    
def input(key):
    print(key)
    if key == 'left mouse down':
        print('pressed left mouse button')
        
        if player5.color == color.black :
            player5.color = color.white
            
        elif player5.color == color.white :
            player5.color = color.black
            
    # if key == Keys.left_mouse_down:   # same as above, but with Keys enum.
    #     print('pressed left mouse button')


# def update():
#     for key, value in held_keys.items():
#         if value != 0:
#             print(key, value)       
       
app.run()