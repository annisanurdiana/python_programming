# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 23:20:57 2021

@author: AnnisaNurdiana and Student ID: 001202000067 >> ODD <<
"""
print("\n===== Week-6 Practice-3 =====\n")
# Variable inner loop
n = 10

# User input
num = input("Enter the number of line: ")

# The outer loop to decide the number of the line
for a in range(int(num),0,-1):
    # The inner loop to generate the variable 'n'
    for b in range(0,a):
        # The value of the variable 'n' will always increase by one (n=n+1).
        n+=1;
        # Display
        print(n, end=' ')
    # Arriage return
    print("\r")

# ctrl+c untuk menghentikan infinite loop pada terminals spyder
