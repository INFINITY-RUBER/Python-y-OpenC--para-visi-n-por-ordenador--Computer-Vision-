import cv2

capture = cv2.VideoCapture(0)

ancho = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# esquina izquierda
x = 330
y = 330

# Dimencion del rectangulo
w = ancho // 4
h = alto // 4

while True:

    resultado, video = capture.read()

    # dibujar rectangulo
    cv2.rectangle(video, (x,y), (x+w, y+h), color=(0,255,0),thickness=4)

    cv2.imshow('Nuestro video rectangulo', video)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


capture.relaase()
cv2.destroyAllWindows()