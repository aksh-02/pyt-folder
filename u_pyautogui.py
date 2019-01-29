# pyautogui.position() to get the co-ordinates of anything on the screen
# pyautogui.click(a, b) to click on the screen at the specified co-ordinates (a, b)

import pyautogui
import time
print('position the mouse')
time.sleep(2)
t = pyautogui.position()
print('you can remove mouse now')
time.sleep(1)
pyautogui.click(t)
