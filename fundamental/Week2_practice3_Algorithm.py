# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 21:00:34 2021

@author: AnnisaNurdiana and Student ID: 001202000067 >> ODD <<

Exercises : Someone can drive a vehicle if they have license and if they are 19 years.
"""
print("\n-------------WEEK-2 Practice-3-------------")

# Get the age input from the user and store it into a variable.
YourAge = int(input("Enter Your Age: "))

# Get the input from the user of they have a driving license
DrivingLicense = str(input("Do you have a diriving license? (yes/no): ").lower())

"""I Little bit explore with syntax >> lower() which is lower() is to returns 
the strings input from the given input by converting each character to lowercase."""

# Check if the user is 19 years old and have a driving license.
if (YourAge >= 19 and DrivingLicense == "yes"): #lowercase yes if they have
    # The user satisfies all requirements
    print("\nCongratulations you are able to drive the vehicle.")
    
# Check if the user is 19 years old but have not a driving license.
elif (YourAge >= 19 and DrivingLicense == "no"): # lowercase no if they don't have
    print("\nSorry! You are unable to drive the vehicle.")
    
# Check if the user is under 19 years old and have not a driving license.
else:
   print("\nSorry! You are unable to drive the vehicle.")
