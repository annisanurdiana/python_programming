# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:20:57 2021

@author: AnnisaNurdiana and Student ID: 001202000067 >> ODD <<
"""
print("\n===== Week-6 Practice-1 =====\n")
# Create a variable
a = 1;
# Create the outer loop to decide the number of the lines
while a <= 10:
    # Create a variable to inner loop
    b = 0
    while b < a:
        print("*", end=' ')
        # The * symbol will always increase every one line.
        b +=1
    # Arriage return
    print("\r")
    # The * symbol will always increase by two for each line.
    a += 2

# ctrl+c untuk menghentikan infinite loop pada terminals spyder
