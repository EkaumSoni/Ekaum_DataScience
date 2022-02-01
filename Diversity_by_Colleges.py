# -*- coding: utf-8 -*-

#Ekaum Soni
#01/26/2022
#College Diversity

import csv
import pandas as pd
DiversityDF = pd.read_csv("diversity_University.csv")


file = open('diversity_University.csv')
DiversityFile = csv.reader(file)
DiversityData = []

header = next(DiversityFile)


for row in DiversityFile:
    DiversityData.append(row)

StateList = []

for row in DiversityData:
    StateList.append(row[2])
StateList = list(set(StateList))


# TOtal Minority per state
for state in range(len(StateList)):
    minorities = []
    totalM = 0
    for row in DiversityData:
        if StateList[state] == row[2]:
            if row[3] != 'Total Minority' and row[3] != 'Women' and row[3] != 'White' and row[3] != 'Unknown' and row[3] != 'Non-Resident Foreign' and row[3] not in minorities:
                minorities.append(row[3])
            if row[3] == 'Total Minority':
                totalM += int(row[4])
    print(str(StateList[state]) + ':', str(totalM))


#Universitys per state

for State in range(len(StateList)):
    Universitys = []
    for row in DiversityData:
        if row[2] == StateList[state] and row[0] not in Universitys:
            Universitys.append(row[0])
    print(str(StateList[state]) + ':' + str(len(Universitys)))

#Largest ethnic group per state

for state in range(len(StateList)):
    MinorityGroup = []
    NumMinority = []
    for row in DiversityData:
        if row[2] == StateList[state] and row[3] != 'Total Minority' and row[3] != 'Women' and row[3] not in MinorityGroup:
            MinorityGroup.append(row[3])
            NumMinority.append(0)
    for i in range(len(MinorityGroup)):
        for row in DiversityData:
            if row[2] == StateList[state] and row[3] == MinorityGroup[i]:
                NumMinority[i] += int(row[4])
    print("The largest ethnic group in " + StateList[state] + 'is ' + str(MinorityGroup[NumMinority.index(max(NumMinority))]) + ': ' + str(max(NumMinority)))

#Race per University
CollegeList = []
for row in DiversityData:
    if row[0] not in CollegeList:
        CollegeList.append(row[0])

for University in range(len(CollegeList)):
    population = 0
    for row in DiversityData:
        if row[0] == CollegeList[University]:
            population += int(row[4])
    for row in DiversityData:
        if row[0] == CollegeList[University] and row[3] != 'Total Minority' and row[3] != 'Women' and row[3] != 'Unknown':
            print(CollegeList[University] + ' is ' + str(round(int(row[4])/population, 2) * 100) + '% ' + row[3])




MinorityList = []
TotalMinority = 0
for row in DiversityData:
    if row[3] =='Total Minority':
        TotalMinority = TotalMinority + int(row[4])
        MinorityList.append(row)

