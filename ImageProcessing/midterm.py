# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 11:54:49 2021

@author: Annisa Nurdiana

"""
import cv2 as cv

img = cv.imread("Lena.bmp", 0)
img2 = cv.imread("baboon.png", 0)

cv.imshow("img", img)
cv.imshow("img2", img2)

for i in range(200):
    for j in range(200):
        if int(img2[img2.shape[0] - 200 + i, img2.shape[1] - 200 + j]) - int(img[i, j]) >= 0:
            img2[img2.shape[0] - 200 + i, img2.shape[1] - 200 + j] = int(img2[img2.shape[0] - 200 + i, img2.shape[1] - 200 + j]) - int(img[i, j])
        else:
            img2[img2.shape[0] - 200 + i, img2.shape[1] - 200 + j] = 0
    
print(img2[img2.shape[0] - 200:img2.shape[0], img2.shape[1] - 200:img2.shape[1]])

cv.imshow("cut", img2)

cv.waitKey(0)