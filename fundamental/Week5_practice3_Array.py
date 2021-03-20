# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:58:51 2021

@author: Annisa Nurdiana and Student ID = 001202000067

Coding and Big Data Lab Module B
"""
print("\n>>---PRACTICE 3 SLICING LIST---<<\n")

# Read the data in the list
numData =  [0, 1, 4, 6, 7, 9, 11, 14, 16, 17]
print(" Display the original data\t\t= ", numData)

# Change the data at a specific index
numData[1]=2;numData[4]=8;numData[5]=10; numData[6:10]=[12,14,16,18]
print(" After change data index \t\t= ", numData)

# Read the sublist from list (slicing)
numData2 =  [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print("\n Display the second data \t\t= ",numData2[0:10])
# Read start from index 5 until the last index
print(" Read the data from index 5  \t= ",numData2[5:])
# Read start from the first index but not until index 7
print(" Read the data until index 6 \t= ",numData2[:7])

# Using list in the list to combine
Data = [[0, 1, 4, 6, 7, 9, 11, 14, 16, 17],[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]]
totalData = (Data[0]+Data[1]); 
# I am using sort() to sorting the data start from the smallest number
totalData.sort() 
# Display Data
print("\n Total data\t= ",len(totalData),"\n Show total data = ",totalData)
# I am using len() in order to know how much data in the list



