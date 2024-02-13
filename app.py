import pyautogui
from time import sleep

#posicao de algo - use o mouseinfo
#fazer algo
pyautogui.moveTo(295,326,duration=2)
for i in range(300):
   sleep(0.5)
   pyautogui.click()