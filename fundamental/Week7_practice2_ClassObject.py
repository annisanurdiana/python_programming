# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 16:03:09 2021

@author: AnnisaNurdiana and Student ID: 001202000067 >> ODD <<

"""

print("\n======================== Week7 - Practice2 ========================\n")

# Create a class called Car.
class Car:
    
    # Declaration of car colors.
    Color = ['Red','Silver','Black']
    
    # Create a tupple structure.
    Car_ = ['Ferrari','BMW','Lexus', 3,2,2]
    
    # Call tupple to the 3rd item of car.
    CarName = Car_[:3]
    # Converts tupple data to a list.
    name = list(CarName)
    # Sort the list by lowest value.
    name.sort()
    
    # Call tupple from the 3rd index.
    CarAge = Car_[3:]
    # Converts tuple data to a list.
    age = list(CarAge)
    # Sort the list by highest value.
    age.sort(reverse=True)
        
    #--------Find The Details of The Car with Dictionary--------#
    
    BMW = {'Name':'BMW',
           'Price': 'Rp789,000,000.00',
           'Color': 'Black',
           'Condition\t':'Second Hand 2 years'
           }
       
    Ferrari = {'Name':'Ferrari',
             'Price': 'Rp10,199,000,000.00',
             'Color': 'Black',
             'Condition':'Second Hand 3 years'
             }
    
       
    Lexus = {'Name':'Lexus',
             'Price': 'Rp11,119,000,000.00',
             'Color': 'Black',
             'Condition':'New!'
             }
    
    #-------------------------------------------------------#
    
    # Method Constructure in Python >> __init__
    def __init__(self,name_,color_,age_):
        self.name_ = name_
        self.color_ = color_
        self.age_ = age_
        
    # Method for accessing attribute values
    def getName_(self):
        return self.name_()
    def getColor_(self):
        return self.color_()
    def getAge_(self):
        return self.age_()
    
    def CarDetail(self):
        print("\tCar Name\t:",self.name_)
        print("\tCar Color\t:",self.color_)
        print("\tCar Age  \t:",self.age_)
    
#------------------------------------------------------------#

print("Wellcome to Yamama Showroom \n",
      "1. Display Car\n",
      "2. Enter New Car\n",
      "3. Seacrh Car Details")
Choose = int(input("Enter Number to Continue: "))

if Choose == 1:
    # Call the programm from Car Class
    print()
    print("Car Name\t\t:",Car.name)
    print("Car Color\t\t:",Car.Color)
    print("Car Age (year)\t:",Car.age)

elif Choose == 2:
    while True:
        carName = input("Enter Name of Car\t\t: "); CN = carName
        carColor = input("Enter Color of Car\t\t: "); CC = carColor
        carCondition = input("Enter Condition of Car\t: "); CD = carCondition
        
        if CN == "" or CC == "" or CD == "":
            print("\n\t>>> INVALID INPUT! <<<")
            break
        
        # Make an Object
        car = Car(CN,CC,CD)
        
        # Call object with all of attribute
        print("\n\t--> NEW CAR DETAILS:")
        print(); car.CarDetail()
        print("\n\t--> NEW CAR ADDED SUCCESSFULLY!!\n")
        
        # Call object with attribute
        print("Success added car name\t:",car.name_);
        print("The color of the car is\t:",car.color_);
        print("The age of the car is\t:",car.age_)
        
        Enter = input("\nClick enter to continue or click \"STOP\" to stop this program = ")
        if Enter == "STOP" or Enter == "Stop" or Enter =="stop":
            print("\n\t>>> Thank you for entering new car here! <<<")
            break

elif Choose == 3:
    Search_by_Name = input("Enter Car Name: ")
    print("\nWhat do you want to know:\n",
          "\n\t Color? \n\t Condition? \n\t Price? \n\t All Details")
    Spesific_Car_Details = input("=== Enter details here: ")
    
    SCD = Spesific_Car_Details; SN =  Search_by_Name
    
    if Spesific_Car_Details == "Color":
        print()
        if SN == "BMW":
            print("The Color of the car = ", Car.BMW["Color"]) 
        elif SN == "Ferrari":
            print("The Color of the car = ",Car.Ferrari["Color"])
        elif SN == "Lexus":
            print("The Color of the car = ",Car.Lexus["Color"])
    elif SCD == "Condition":
        print()
        if SN == "BMW":
             print("The Condition of the car = ",Car.BMW["Condition"])
        elif SN == "Ferrari":
             print("The Condition of the car = ",Car.Ferrari["Condition"])
        elif SN == "Lexus":
             print("The Condition of the car = ",Car.Lexus["Condition"])
    elif SCD == "Price":
        print()
        if SN == "BMW":
            print("The Price of the car = ",Car.BMW["Price"])
        elif SN == "Ferrari":
             print("The Price of the car = ",Car.Ferrari["Price"])
        elif SN == "Lexus":
              print("The Price of the car = ",Car.Lexus["Price"])
    elif SCD == "" or SCD =="All Details":
        print()
        if SN == "BMW":
            for x,y in Car.BMW.items():
                print(x +":"+y); print()
            print()
        elif SN == "Ferrari":
            for x,y in Car.Ferrari.items():
                print(x +":"+y); print()
            print()
        elif SN == "Lexus":
            for x,y in Car.Lexus.items():
                print(x +":"+y); print()
            print()
    else:
        print("\n>>> INVALID INPUT! <<<")
        
else:
    print(">>> INVALID <<<")
    
print("---------------------------------------------------------")


















