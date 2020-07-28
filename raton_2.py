import numpy as np
import cv2

# variables globales 
dibujando = False
valorx = 0
valory = 0

# definimos nuestras funciones para dibujar
def dibujar(event, x, y, etiquetas, parametros):
    global dibujando, valorx, valory

    if event == cv2.EVENT_LBUTTONDOWN:# BOTON IZQUIERDO MOUSE PRESIONADO
        dibujando = True
        valorx = x
        valory = y
    elif event == cv2.EVENT_MOUSEMOVE: # evento al mover el mause
        if dibujando == True:
            cv2.rectangle(imagen, (valorx, valory), (x, y),(255,0,0),-1)
    elif event == cv2.EVENT_LBUTTONUP:# BOTON IZQUIERDO MOUSE SOLTADO
        dibujando = False
        cv2.rectangle(imagen, (valorx, valory), (x, y),(255,0,0),-1)


# conectar la imagen con la funcion
cv2.namedWindow(winname='mi_imagen')
cv2.setMouseCallback('mi_imagen', dibujar)

# mostra imagenes
imagen = np.zeros(shape=(500, 500, 3), dtype=np.int8)

while True:
    cv2.imshow('mi_imagen', imagen)

    if cv2.waitKey(10) & 0xFF == 27: # tecla escape
        break