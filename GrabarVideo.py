import cv2

capture = cv2.VideoCapture(0)

ancho = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# grabar video mac
codigo = cv2.VideoWriter_fourcc(*'MJPG')
grabador = cv2.VideoWriter('video.avi', codigo, 20,(ancho, altura))

# grabar video Windows
#codigo = cv2.VideoWriter_fourcc(*'DIVX')
#grabador = cv2.VideoWriter('video.mp4', codigo, 20,(ancho, altura))

while True:
    resultado, video = capture.read()

    # grabacion video
    grabador.write(video)


    cv2.imshow('Nuestro video', video)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.relaase()
grabador.relaase()
cv2.destroyAllWindows()
