# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:31:51 2021

@author: Annisa Nurdiana
"""

import cv2 as cv
#---Logic Operation - XOR & NOT
picture1 = cv.imread('Lena.bmp')
picture2 = cv.imread('baboon.png')

# Resize to 530 x 680
picture1_resize = cv.resize(picture1, (530,680))
picture2_resize = cv.resize(picture2, (530,680))

# Bitwise XOR
picture_xor = cv.bitwise_xor (picture1_resize, picture2_resize, mask = None)

# Bitwise NOT
picture_not = cv.bitwise_not (picture1_resize, picture2_resize, mask = None)

cv.imshow('Baboon', picture_xor)
cv.imshow('Lena', picture_not)

cv.waitKey(0)
