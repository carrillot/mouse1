from random import *
import pyautogui as py
import matplotlib.pyplot as plt
import numpy as np
from numpy import savetxt
import axies
import logica
import funtion

print("EMPIEZA")
# contador = 0
# while True:
#     print(contador)
#     contador += 1
#     if contador > 500:
#         break
#
#     funtion.screen_shot()
#     cartas = axies.axie_tanke()
#     logica.logica(cartas)


funtion.screen_shot()
cartas = axies.axie_tanke()
logica.logica(cartas)


for carta in cartas:
    print("B")
    funtion.localizar_imagen(carta)














# empieza rapido y termina despacio
# https://recursospython.com/guias-y-manuales/pyautogui/
# https://stackoverflow.com/questions/61334727/python-human-like-mouse-behaviour
# py.moveTo(720, 360, uniform(1, 50), py.easeOutQuad)

# Cargar OpenCV
import cv2
# Sirve para operar con cualquier dato numérico
import numpy as np

# # Leer las imágenes que vamos a comparar
# # Imagen sobre la que vamos a detectar si existe otra imagen
# img_rgb = cv2.imread('1.PNG')
# # Imagen que comprobamos si existe en la imagen Todo
# template = cv2.imread('3.PNG')
#
# # Tamaño de la imagen 1.jpg
# w, h = template.shape[:-1]
#
# # Función que sirve para detectar si una imagen está contenida en otra
# res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
#
# # Umbral admitido
# threshold = .7
#
# # Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
# loc = np.where(res >= threshold)
# result = tuple([tuple(e) for e in loc])
# MyTuple2 = ( )
#
# if result[0] == MyTuple2:
#     print("NO HAY IMAGEN")
# else:
#     print("HAY IMAGEN")

