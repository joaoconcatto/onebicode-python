import pyautogui as pygui
import time

def calculadora():
    pygui.press('winleft')
    time.sleep(3)
    pygui.write('calculadora')
    time.sleep(3)
    pygui.press('enter')

def gerenciador_tarefas():
    pygui.hotkey('ctrl', 'shift', 'esc')

def tela_esquerda():
    with pygui.hold('winleft'):
        pygui.press('left')
    
    time.sleep()


calculadora()
gerenciador_tarefas()
tela_esquerda()