# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:20:33 2021

@author: Annisa Nurdiana
"""

import cv2 as cv
import numpy as np

img = cv.imread('Lena.bmp')

original = img.copy()
xp = [0, 64, 128, 192, 255]
fp = [0, 16, 128, 240, 255]
x = np.arange(256)

table = np.interp(x, xp, fp).astype('uint8')
img = cv.LUT(img, table)

cv.imshow("Original", original)
cv.imshow("Output", img)
cv.waitKey(0)
cv.destroyAllWindows() 