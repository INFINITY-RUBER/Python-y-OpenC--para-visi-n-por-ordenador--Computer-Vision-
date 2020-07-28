import numpy as np
import cv2

# defimos la funcio dibujar con el raton
def dibujar(event, x, y, etiquetas, parametros):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen, (x,y), 10, (255,0,0),-1)
        
# conectar la imagen con la funcion
cv2.namedWindow(winname='mi_imagen')
cv2.setMouseCallback('mi_imagen', dibujar)

# mostra imagenes
imagen = np.zeros(shape=(500, 500, 3), dtype=np.int8)

while True:
    cv2.imshow('mi_imagen', imagen)
    if cv2.waitKey(10) & 0xFF == 27: # tecla escape
        break
cv2.destroyAllWindows()    
