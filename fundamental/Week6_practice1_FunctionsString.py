# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 13:44:44 2021

@author: AnnisaNurdiana and Student ID: 001202000067 >> ODD <<
"""
print("\n=================== Week6 - Practice1b ===================")

# Initializing a function name "Student" With two parameter integer
def Student(int_1,int_2):
    return int(int_1)*int(int_2)

# Enter user's input as a string
int_1 = input("\nEnter the first number to last digit of your student id: ")
int_2 = input("\nEnter the second number to last digit of your student id: ")

# Display Student function and convert string input to integer 
print("\n>>> The result is ", Student(int_1,int_2))

