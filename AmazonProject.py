#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 09:09:49 2022

@author: ekaumsoni
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

file = open('Amazon.csv')
AmazonFile = csv.reader(file)

header = next(AmazonFile)

AmazonData = []

for row in AmazonFile:
    AmazonData.append(row)


AmazonArray = np.array(AmazonData)


# Total amount of money spent
TotalArray = AmazonArray[:,29]
TotalSpentList = []
TotalSpent = 0
for row in TotalArray:
        value = row[1:]
        TotalSpentList.append(value)
        TotalSpent += float(value)
        


print("My total amount spent is $"+ str(round(TotalSpent,2)))


TotalSpentArray = np.array(TotalSpentList)
TotalSpentArray = TotalSpentArray.astype(float)

# Min and Max
print("Min: $", round(np.amin(TotalSpentArray), 2))
print("Max: $", round(np.amax(TotalSpentArray), 2))

#Median and Mean
print("Median: $", round(np.median(TotalSpentArray), 2))
print("Mean: $", round(np.average(TotalSpentArray), 2))

#Taxes
totalTax = 0
for row in AmazonArray:
        value = row[28]
        value = value[1:]
        totalTax += float(value)
print("total tax: ", round(totalTax, 2))
print("effective tax rate: ", round(totalTax/18, 2), "%")

#Orders per Year
Order16 = 0
Order17 = 0 
Order18 = 0 
Order19 = 0 
Order20 = 0 
Order21 = 0 
Order22 = 0 

DateArray = AmazonArray[:,0]

for row in DateArray:
    if row[6:] == '16':
        Order16 +=1
    elif row[6:] == '17':
        Order17 +=1
    elif row[6:] == '18':
        Order18 +=1
    elif row[6:] == '19':
        Order19 +=1
    elif row[6:] == '20':
        Order20 +=1
    elif row[6:] == '21':
        Order21 +=1
    elif row[6:] == '22':
        Order22 +=1

OrdersList = []
OrdersList.append(Order16)
OrdersList.append(Order17)
OrdersList.append(Order18)
OrdersList.append(Order19)
OrdersList.append(Order20)
OrdersList.append(Order21)
OrdersList.append(Order22)         

       
x = [2016,2017,2018,2019,2020,2021,2022]
plt.bar(x ,OrdersList)

plt.title('Purchases Per Year')
plt.xlabel('Year')
plt.ylabel('Purchases')

plt.show()