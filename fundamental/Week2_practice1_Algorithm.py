# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:59:25 2021

@author: AnnisaNurdiana and Student ID: 001202000067 >> ODD <<

Exercises: Create a program that let the user input user birth year.
"""
print("\n-------------WEEK-2 Practice-1-------------")

# Define the current year and store it into a variable.
CurrentYear = 2018
# Get the user input and store it into a variable (don’t forget to convert the input to integer)
Name = str(input("Enter your name \t: "))
BirthYear = int(input("Enter year of birth : "))
# Calculate the age (current year - birth year) and store it into a variable.
Age = CurrentYear - BirthYear
# Display the user age.
print("\nHello ",Name,", you are ", Age," years old.\n")
