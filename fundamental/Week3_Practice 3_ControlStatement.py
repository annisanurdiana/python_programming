# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 17:12:17 2021

@author: Annisa Nurdiana and Student ID = 001202000067

Coding and Big Data Lab Module B

"""

# Ask for the user's height from input function.
Height = int(input(" Please Enter Your Height: "))

# If the input height greater than or equal to "125" then print
if Height >= 125:
    if Height == 125:
         print(' You must be accompanied by an older person.')
    else:
        print(' You can enter the roller coaster rides.')
else:
    print(' Sorry your height is not enough for roller coaster ride requirement.')
