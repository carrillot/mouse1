import cv2
import numpy as np
import pyautogui
from random import *
import secrets
import random
global str

def screen_shot():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("capturas/todo1.PNG", image)


def localizar_imagen(carta):
    img = pyautogui.locateOnScreen('capturas/{}'.format(carta), confidence=0.9, grayscale=True)
    print("Coordenadas imagenes")

    center = pyautogui.center(img)
    mover_raton(center)
    pyautogui.moveTo(center)


def mover_raton (center):
    foo = ['easeInQuad', 'easeOutQuad', 'easeInOutQuad', 'easeInBounce', 'easeInElastic']
    b = secrets.choice(foo)
    x = b
    lista = [1, 2, 3]
    coor_x = center[0]
    coor_y = center[1]
    inicio = random.sample(lista, 1)[0]
    final = random.sample(lista, 1)[0]

    if x == "easeInQuad":
        print("1")
        pyautogui.moveTo(coor_x, coor_y, uniform(inicio, final), pyautogui.easeInQuad)
    elif x == "easeOutQuad":
        print("2")
        pyautogui.moveTo(coor_x, coor_y, uniform(inicio, final), pyautogui.easeOutQuad)
    elif x == "easeInOutQuad":
        print("3")
        pyautogui.moveTo(coor_x, coor_y, uniform(inicio, final), pyautogui.easeInOutQuad)
    elif x == "easeInBounce":
        print("4")
        pyautogui.moveTo(coor_x, coor_y, uniform(inicio, final), pyautogui.easeInBounce)
    elif x == "easeInElastic":
        print("5")
        pyautogui.moveTo(coor_x, coor_y, uniform(inicio, final), pyautogui.easeInElastic)
    # >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
    # >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
    # >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
    # >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
    # >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end