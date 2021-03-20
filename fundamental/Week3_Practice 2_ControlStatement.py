# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 17:12:16 2021

@author: Annisa Nurdiana and Student ID = 001202000067

Coding and Big Data Lab Module B

"""
# Ask for the user's math score from input function.
MathScore = int(input(" Please enter your math score: "))

# If the input math score greater than "98" then print
if MathScore  > 98:
    print(' Woah, goodluck in your math olympics!')
elif MathScore  == 98:
    print(' You still can register for the math olympics.')
else:
     print(' Sorry you can\'t register for the math olympiad yet!')
