# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 04:08:40 2021

@author: Annisa Nurdiana and Student ID = 001202000067

Coding and Big Data Lab Module B 

Odd Print set of numbers from 50 to 80 with step = 3, if meet 62, continue.
"""
print("\n---PRACTICE 2 FOR LOOP ---\n")

# for loop will start from number 50 and stop in 80
for number in range (50,80):
    # if number is 62, it will be continue
    if number == 62:
        continue
    print(number, end=" ")
