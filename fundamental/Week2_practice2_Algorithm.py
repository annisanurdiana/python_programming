# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 21:00:12 2021

@author: AnnisaNurdiana and Student ID: 001202000067 >> ODD <<

Exercises: Only a person above 18 years old that able to create national id
"""
print("\n-------------WEEK-2 Practice-2-------------")

# Take the input from the user and store it into a variable.
Name = str(input("Enter Name \t: ")); Age = int(input("Enter Age \t: "))
# Determine if the input (age) is greater than 18 or not.
if (Age > 18):
    # If the input (age) is greater than 18
    print();print("Hello ", Name,". You are able to create a national id :)")
else:
    # Else, if the input (age) is not greater than 18
    print();print("Sorry ", Name,". You are not able to create a national id :(")
    