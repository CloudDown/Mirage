import os
import pyautogui
from time import sleep
from PIL import ImageGrab

########
n = 1
t = 0.3
virus=r"\virus_exemple.bat"
desktop=True
########

program_path = os.path.dirname(os.path.abspath(__file__))
print(program_path)
os.system("start"+" "+program_path+virus)
if desktop == True:
    pyautogui.hotkey('win', 'd')
pict = ImageGrab.grab()
image_path = os.path.join(program_path, "screen.png")
pict.save(image_path)

for i in range(n):
    os.system(r"start "+" "+image_path)
    sleep(t)
    pyautogui.press('f11')