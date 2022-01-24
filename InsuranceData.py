# -*- coding: utf-8 -*-
#Ekaum Soni
#01/24/2022
#
#Preparing Data Sets
import csv, os


# os.system('clear')
# #Pandas is superior
# import pandas as pd
# insuranceCSV = pd.read_csv("insurance_data - insurance.csv")

file = open('insurance_data - insurance.csv')
insuranceFile = csv.reader(file)


#Bring up next value
header = next(insuranceFile)

insuranceData = []


#Make one whole list out of every separate list
for row in insuranceFile:
    insuranceData.append(row)

#Change Female to 0, Male to 1

for row in insuranceData:
    if row[1] == 'female':
        row[1] = 0
    if row[1] == 'male':
        row[1] = 1


for row in insuranceData:
    if row[4] == 'no':
        row[4] = 0
    if row[4] == 'yes':
        row[4] = 1

#Add Insurance Cost to List

for row in insuranceData:
    insurance_cost = 250*int(row[0]) - 128*int(row[1]) + 370*float(row[2]) + 425*int(row[3]) + 24000*int(row[4]) - 12500
    insurance_cost = int(insurance_cost*100)/100
    row.append(insurance_cost)
    
#Create List with averages of 4 regions

Southwest_Total = 0 
Northeast_Total = 0 
Southeast_Total = 0
Northwest_Total = 0
countNE = 0 
countSE = 0
CountNW = 0
CountSW = 0


for row in insuranceData:
    if row[5] == 'northeast':
        Northeast_Total += row[7] 
        countNE +=1
        NE_AVG = Northeast_Total/countNE
    if row[5] == 'southeast':
        Southeast_Total += row[7] 
        countSE +=1
        SE_AVG = Southeast_Total/countSE
    if row[5] == 'northwest':       
        Northwest_Total += row[7] 
        CountNW += 1
        NW_AVG = Northwest_Total/CountNW
    if row[5] == 'southwest':
        Southwest_Total += row[7] 
        CountSW += 1
        SW_AVG = Southwest_Total/CountSW

Region_AVG = [NE_AVG, SE_AVG, NW_AVG, SW_AVG]

#Create a last with Only Females, and one with Only Males
List_Female = []
List_Male = []

for row in insuranceData:
    if row[1] == 'female':
        List_Female.append(row)
    if row[1] == 'male':
        List_Male.append(row)


#Create a list with only Smokers, and one with non Smokers
List_Smokers  = []
List_NonSmokers = []


for row in insuranceData:
    if row[4] == 'no':
        List_NonSmokers.append(row)
    if row[4] == 'yes':
        List_Smokers.append(row)

