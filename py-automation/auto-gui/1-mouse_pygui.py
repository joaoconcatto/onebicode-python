import pyautogui
from pyautogui import mouseInfo
import time

# 1- tamanho da tela
print(pyautogui.size())


# 2- pegar a posição atual do cursor
print(pyautogui.position())


# 3- App para ver a posição do mouse em tempo real
# mouseInfo()


# 4- mover o cursor do mouse
pyautogui.moveTo(1803, 12, 2)
time.sleep(3)
pyautogui.click()


# 5- realizando o scroll
time.sleep(3)
pyautogui.moveTo(940,474)