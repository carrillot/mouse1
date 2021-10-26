# Cargar OpenCV
import cv2
# Sirve para operar con cualquier dato numérico
import numpy as np
import sys
import time
import cuenta1

def leer_carta(carta):
    # Leer las imágenes que vamos a comparar
    # Imagen sobre la que vamos a detectar si existe otra imagen
    img_rgb = cv2.imread('capturas/todo1.PNG')
    # Imagen que comprobamos si existe en la imagen Todo
    template = cv2.imread("capturas/{}".format(carta))

    # Tamaño de la imagen 1.jpg
    w, h = template.shape[:-1]

    # Función que sirve para detectar si una imagen está contenida en otra
    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)

    # Umbral admitido
    threshold = .7

    # Si está dentro del umbral, crear un cuadrado sobre la imagen contenida en la imagen Todo
    loc = np.where(res >= threshold)
    result = tuple([tuple(e) for e in loc])
    MyTuple2 = ( )
    if result[0] == MyTuple2:
        # print("NO HAY IMAGEN")
        carta = ""
    else:
        # print("HAY IMAGEN")
        carta = carta


    # if 'victoria.PNG' or "defeated.PNG" in carta:
    if 'victoria.PNG' in carta:
        print("SALIMOSSSSSSSS")
        sys.exit()
    if 'defeated.PNG' in carta:
        print("SALIMOSSSSSSSS")
        sys.exit()


    return carta

    # return carta


def axie_tanke():
    print("Entra en el axie tanque")
    # lista_cartas = ["bug_noise.PNG","headshot.PNG","peace_treaty.PNG","risky_feather.PNG","victoria.PNG","defeated.PNG","carrot_hummer.PNG","prickly_trap.PNG","chomp.PNG","october_treat.PNG"]
    lista_cartas = cuenta1.cuenta()

    thislist = []

    for i in lista_cartas:
        carta = leer_carta(i)
        thislist.append(carta)

    thislist = [i for i in thislist if i]

    return thislist
