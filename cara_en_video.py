import numpy as np
import matplotlib.pyplot as plt
import cv2

cascada_eye = cv2.CascadeClassifier('haarcascade_eye.xml')
cascada_cara = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detectar_cara(imagen):
    imagen1 = imagen.copy()
    rectangulos = cascada_cara.detectMultiScale(imagen1)
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1,(x,y),(x+w,y+h),(255,0,0),10)
    return imagen1

def detectar_ojos(imagen):
    imagen1 = imagen.copy()
    rectangulos = cascada_eye.detectMultiScale(imagen1)
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1,(x,y),(x+w,y+h),(255,0,0),10)
    return imagen1


capture = cv2.VideoCapture(0)

while True:
    res, video = capture.read()
    video = detectar_cara(video)
    video = detectar_ojos(video)
    
    cv2.imshow('Detectecion rostro en video', video)
    tecla = cv2.waitKey(1)
    if tecla == 27:
        break


capture.relaase()
cv2.destroyAllWindows()

