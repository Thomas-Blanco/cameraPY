import cv2 as cv



captureVideo = cv.VideoCapture(0)

if not captureVideo.isOpened():
    print("No se encontro una camara")
    exit()
while True:
    #Leer camara
    _, camera=captureVideo.read()
    greys = cv.cvtColor(camera, cv.COLOR_BGR2GRAY)
    #Mostrar camara
    cv.imshow("Camera", greys)
    #Para cerrar
    if cv.waitKey(1)==ord("q"):
        break
captureVideo.release()
cv.destroyAllWindows()

