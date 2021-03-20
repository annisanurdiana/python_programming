# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 13:44:48 2021

@author: AnnisaNurdiana and Student ID: 001202000067 >> ODD <<
"""
print("\n=================== Week6 - Practice3b ===================")

# Command to enter the user's input as username
username =  input("Enter User's Name Here\t: ")

# Command to enter the user's input as number
num1 = int(input("Enter First number\t\t: "));
num2 = int(input("Enter Second number\t\t: "))
num3 = int(input("Enter Third number\t\t: "));
num4 = int(input("Enter Fourth number\t\t: "))

# Declare result with this formula >>> (a*b^c)/d >>> ODD
result = (num1 * num2**num3)/num4

# Initialize a string and use format() to fill in the placeholders
Variable = "\nMy name is {}, The result is {}".format(username,result)

# Display the string (Variable)
print(Variable)

