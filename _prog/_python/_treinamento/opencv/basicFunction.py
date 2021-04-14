# carrega as bibliotecas
import cv2
import numpy as np

kernel = np.ones((5), np.uint8) # cria o kernel

# carrega e modifica imagens
img = cv2.imread('betix.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

# apresenta imagens na tela
cv2.imshow('Image Gray', imgGray)
cv2.imshow('Image Blur', imgBlur)
cv2.imshow('Image Canny', imgCanny)
cv2.imshow('Image Dialation', imgDialation)
cv2.imshow('Image Eroded', imgDialation)

# evento para fechar janela
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
