# -*- coding: utf-8 -*-

#Ekaum Soni
#01/26/2022
#College Diversity

import csv
import pandas as pd
DiversityDF = pd.read_csv("diversity_school.csv")


file = open('diversity_school.csv')
DiversityFile = csv.reader(file)
DiversityData = []

header = next(DiversityFile)


for row in DiversityFile:
    DiversityData.append(row)

StateList = []

for row in DiversityData:
    StateList.append(row[2])
StateList = list(set(StateList))

MinorityList = []
TotalMinority = 0
for row in DiversityData:
    if row[3] =='Total Minority':
        TotalMinority = TotalMinority + int(row[4])
        MinorityList.append(row)

