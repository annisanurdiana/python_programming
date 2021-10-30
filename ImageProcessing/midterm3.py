# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:26:36 2021

@author: Annisa Nurdiana
"""
import cv2 as cv
import numpy as np

image = cv.imread('Lena.bmp')
image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

increase = 100

v = image[:, :, 2]
v = np.where(v <= 255 - increase, v + increase, 255)
image[:, :, 2] = v

image = cv.cvtColor(image, cv.COLOR_HSV2BGR)

cv.imshow('Brightness', image)
cv.waitKey(0)
cv.destroyAllWindows()