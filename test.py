import pyautogui
import random
import scipy
import time
from scipy import interpolate
from random import *
import secrets
import random
global str


foo = ['easeInQuad', 'easeOutQuad', 'easeInOutQuad', 'easeInBounce', 'easeInElastic']
b = secrets.choice(foo)
x = b
lista = [1,2,3,4,5]

inicio = random.sample(lista,  1)[0]
final = random.sample(lista,  1)[0]


if x == "easeInQuad":
    print("1")
    pyautogui.moveTo(300, 200, uniform(inicio, final), pyautogui.easeInQuad)
elif x == "easeOutQuad":
    print("2")
    pyautogui.moveTo(300, 200, uniform(inicio, final), pyautogui.easeOutQuad)
elif x == "easeInOutQuad":
    print("3")
    pyautogui.moveTo(300, 200, uniform(inicio, final), pyautogui.easeInOutQuad)
elif x == "easeInBounce":
    print("4")
    pyautogui.moveTo(300, 200, uniform(inicio, final), pyautogui.easeInBounce)
elif x == "easeInElastic":
    print("5")
    pyautogui.moveTo(300, 200, uniform(inicio, final), pyautogui.easeInElastic)
# >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
# >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
# >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
# >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
# >>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end