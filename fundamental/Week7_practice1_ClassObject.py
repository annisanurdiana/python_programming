# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:02:33 2021

@author: AnnisaNurdiana and Student ID: 001202000067 >> ODD <<

"""

print("\n========================== Week7 - Practice1 ==========================\n")

# Create a class called Car.
class Car:
    
    # Declaration of car colors.
    Color = ['Red','Silver','Black','Blue']
    
    # Create a tupple structure.
    Car_ = ['Mercedes-Benz','Ferrari','Rolls-Royce','Lexus',
               3,4,1,2]
    
    # Call tupple to the 4th items.
    CarName = Car_[:4]
    # Converts tupple data to a list.
    name = list(CarName)
    # Sort the list by lowest value.
    name.sort()
    
    # Call tupple from the 4th index.
    CarAge = Car_[4:]
    # Converts tupple data to a list.
    age = list(CarAge)
    # Sort the list by highest value.
    age.sort(reverse=True)
    
    #--------Find The Details of The Car with Dictionary--------#
    
    Car_1 = {'Name\t\t':'Mercedes-Benz',
             'Price\t\t': 'Rp689,000,000.00',
             'Color\t\t': 'Black',
             'Condition\t':'Second Hand 2 years'
             }
       
    Car_2 = {'Name\t\t':'Ferrari',
             'Price\t\t': 'Rp10,199,000,000.00',
             'Color\t\t': 'Black',
             'Condition\t':'Second Hand 3 years'
             }
    
       
    Car_3 = {'Name\t\t':'Lexus',
             'Price\t\t': 'Rp11,119,000,000.00',
             'Color\t\t': 'Black',
             'Condition\t':'New!'
             }
    
    Car_4 = {'Name\t\t':'Rolls-Royce',
             'Price\t\t': 'Rp5,199,000,000.00',
             'Color\t\t': 'Black',
             'Condition\t':'Second Hand 1 years'
             }
    
    #------------------------------------------------------------#
    
# Call the programm from Car Class
print("Car Name\t\t:",Car.name)
print("Car Color\t\t:",Car.Color)
print("Car Age (year)\t:",Car.age)
print("\n----------------------------- Car Details -----------------------------\n")

# Show car details of the dictionary in the class car
for x,y in Car.Car_1.items():
    print(x +":"+y)
print()
for x,y in Car.Car_2.items():
    print(x +":"+y)
print()
for x,y in Car.Car_3.items():
    print(x +":"+y)
print()
for x,y in Car.Car_4.items():
    print(x +":"+y)
    





