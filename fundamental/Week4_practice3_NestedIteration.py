# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 04:08:42 2021

@author: Annisa Nurdiana and Student ID = 001202000067

Coding and Big Data Lab Module B
"""
print("\n---PRACTICE 3 NESTED ITERATION ---\n")

# A declaration starting at 1 as a start, 11 as a stop, and 1 as a step
# Step = the amount the variable value increases.
for x in range (1,11,1):
    # Print values will start from line one by one, line two will be 
    # increased by two, and will increased until the 10th line.
    for y in range(1,x+1):
        print(y+0, end =' ')
    print("\r")
    