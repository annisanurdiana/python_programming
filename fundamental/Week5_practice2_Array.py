# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:58:51 2021

@author: Annisa Nurdiana and Student ID = 001202000067

Coding and Big Data Lab Module B
"""
print("\n>>---PRACTICE 2 ADDING NEW LIST ITEMS---<<\n")

# Initialize a list with these items 
# 'Toyota', 'BMW', 'Volvo', 'Volkswagen', 'Fiat'. 
Cars =  ["Toyota", "BMW", "Volvo", "Volkswagen", "Fiat"]
print(" The Cars List Original: ",Cars)

# Delete 'Volvo' and 'Flat' from the Car list
print("\n Delete 'Volvo' from Car list!", Cars.remove("Volvo"),
      "\n Delete 'Volvo' from Car list!", Cars.pop())

# Display Cars after delete
print("\n Cars List after delete: ", Cars)

# Input 'Chrysler' and 'Renault' to the Car list
print("\n Input 'Chrysler' to the Car list!",Cars.insert(3,'Chrysler'),
      "\n Input 'Renault' to the Car list!",Cars.append('Renault'))

# Display car list after delete and add new cars
print("\n The Cars List Updated: ",Cars)

