import keyboard
import pyautogui
import time


keyboard.press_and_release('windows+ r')
pyautogui.moveTo(50,1000)

keyboard.write('microsoftedge')
#time.sleep(2)
keyboard.press_and_release('enter')

time.sleep(2)
keyboard.press_and_release('windows+Up')
#time.sleep(2)
keyboard.press_and_release('ctrl+shift+n')
#time.sleep(2)
#keyboard.press_and_release('ctrl+l')
keyboard.write("python")
keyboard.press_and_release('enter')
time.sleep(1)
#pyautogui.moveTo(100,300,duration=1)
pyautogui.click(100,300,duration=1)
keyboard.press_and_release('tab')
keyboard.press_and_release('tab')
keyboard.press_and_release('tab')
keyboard.press_and_release('tab')
keyboard.press_and_release('tab')
keyboard.press_and_release('tab')
keyboard.press_and_release('tab')
keyboard.press_and_release('tab')
keyboard.press_and_release('enter')
