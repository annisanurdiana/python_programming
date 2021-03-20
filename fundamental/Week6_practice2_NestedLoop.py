# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:20:57 2021

@author: AnnisaNurdiana and Student ID: 001202000067 >> ODD <<
"""

print("\n===== Week-6 Practice-2 =====\n")
# Create a variable
a = 1;

# Create the outer loop to decide the number of the lines
while a <= 12:
    # Create variable 'b' for the inner loop
    b = 0
    # Create variable 'c' for the inner loop
    c = 0
    while b < a:
        # Each row value of the variable 'c' will always increase by one.
        c += 1
        print(c, end=' ')
         # The 'c' variable will always increase every one line.
        b +=1
    # Arriage return
    print("\r")
    # The 'a' variable will always increase by two numbers for each line.
    a += 2

# ctrl+c untuk menghentikan infinite loop pada terminals spyder
