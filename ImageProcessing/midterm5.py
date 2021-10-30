# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:50:11 2021

@author: Annisa Nurdiana
"""

import cv2 as cv

img = cv.imread("Lena.bmp", 0)
img2 = cv.imread("Baboon.png", 0)

cv.imshow("FirstOriginal.Img",img)
cv.imshow("SecondOriginal.Img",img2)

pic = img[:200,:200]
pic2 = img2[img2.shape[0]-200:img2.shape[0],img2.shape[1]-200:img2.shape[1]]

cv.imshow("FirstImage",pic)
cv.imshow("SecondImage",pic2)

for i in range(200):
    for j in range(200):
        if int(pic2[i,j]) - int(pic[i,j]) < -1:
            pic2[i,j] = int(pic2[i,j]) - int(pic[i,j])
        else:
            pic2[i,j] = 0

cv.imshow("Result", pic2)

cv.waitKey(0)
cv.destroyAllWindows()