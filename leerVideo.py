import cv2

capture = cv2.VideoCapture('video.avi')

if capture.isOpened() == False:
    print('Error al abrir el video')

while capture.isOpened():

    resultado, video = capture.read()

    if resultado == True:

        cv2.imshow('Mi video', video)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 

    else:
        break

capture.relaase()
cv2.destroyAllWindows()