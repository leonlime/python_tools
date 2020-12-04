#!/usr/bin/env python 
import cv2
import numpy as np

imagem1 = cv2.imread('bomba3.jpeg')
imagem2 = cv2.imread('bomba3.jpeg')
imagem3 = cv2.imread('bomba3.jpeg')

classificador1 = cv2.CascadeClassifier('cascade2.xml')
classificador2 = cv2.CascadeClassifier('cascade4.xml')
classificador3 = cv2.CascadeClassifier('cascade5.xml')

imagemcinza = cv2.cvtColor(imagem1, cv2.COLOR_BGR2GRAY)

# deteccoes1 = classificador1.detectMultiScale(imagemcinza)
# deteccoes2 = classificador2.detectMultiScale(imagemcinza)
# deteccoes3 = classificador3.detectMultiScale(imagemcinza)

deteccoes1 = classificador1.detectMultiScale(imagemcinza, scaleFactor=1.1,
                                           minNeighbors=100,
                                           minSize=(10,10),
                                           maxSize=(3000,3000))

deteccoes2 = classificador2.detectMultiScale(imagemcinza, scaleFactor=1.1,
                                           minNeighbors=100,
                                           minSize=(10,10),
                                           maxSize=(3000,3000))

deteccoes3 = classificador3.detectMultiScale(imagemcinza, scaleFactor=1.1,
                                           minNeighbors=100,
                                           minSize=(10,10),
                                           maxSize=(3000,3000))


for (x, y, l, a) in deteccoes1:
    cv2.rectangle(imagem1, (x, y), (x + l, y + a), (0,255,0), 2)

for (x, y, l, a) in deteccoes2:
    cv2.rectangle(imagem2, (x, y), (x + l, y + a), (0,255,0), 2)

for (x, y, l, a) in deteccoes3:
    cv2.rectangle(imagem3, (x, y), (x + l, y + a), (0,255,0), 2)

cv2.imshow('class 1', imagem1)
cv2.imshow('class 2', imagem2)
cv2.imshow('class 3', imagem3)

cv2.waitKey(0)
cv2.destroyAllWindows()

# deteccoes = classificador.detectMultiScale(imagemcinza, scaleFactor=1.1,
#                                            minNeighbors=20,
#                                            minSize=(100,100),
#                                            maxSize=(3000,3000))

# deteccoes = classificador.detectMultiScale(imagemcinza, scaleFactor=1.1,
#                                            minNeighbors=21,
#                                            minSize=(5,5),
#                                            maxSize=(3000,3000))                                           

# print(deteccoes)
# print(len(deteccoes))

# for (x, y, l, a) in deteccoes:
#     cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)

# cv2.imshow('Detector de faces', imagem)
# cv2.waitKey(0)
# cv2.destroyAllWindows()