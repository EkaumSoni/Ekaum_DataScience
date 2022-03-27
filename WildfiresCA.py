#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 09:39:46 2022

@author: ekaumsoni
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Convert CSV to Dataframe
Wildfires_DF = pd.read_csv('Wildfires.csv')
Pollution_DF = pd.read_csv('pollution_us_2000_2016.csv')

# Wildfires per year
Wildfires_DF['YEAR_'] = Wildfires_DF['YEAR_'].dropna().astype(int)
FiresPerYear = Wildfires_DF.groupby(['YEAR_']).count()
plt.plot(FiresPerYear['OBJECTID'])

#Wildfires post 2000
WF2k = Wildfires_DF[Wildfires_DF['YEAR_']>= 2000]
FiresPerYear2k = WF2k.groupby(['YEAR_']).count()
plt.plot(FiresPerYear2k['OBJECTID'])

#How many Acres were burned each year
Wildfires_DF['GIS_ACRES'] = Wildfires_DF['GIS_ACRES'].dropna().astype(int)
SizeofFire = Wildfires_DF.groupby('YEAR_')['GIS_ACRES'].sum()
plt.plot(SizeofFire)

#Average Size of Forest burned eah year 
AverageSize = Wildfires_DF.groupby('YEAR_')['GIS_ACRES'].mean()
plt.plot(AverageSize)

# Most common cause of Wildfires
Wildfires_DF['CAUSE'] = Wildfires_DF['CAUSE'].dropna().astype(int)
Cause = Wildfires_DF.groupby(['CAUSE']).count()
plt.plot(Cause.index, Cause['OBJECTID'])

#Pollution in California
CA_Pollution = Pollution_DF[Pollution_DF['State'] == 'California']

AveragePollution = CA_Pollution.groupby(pd.DatetimeIndex(CA_Pollution['Date Local']).year)['CO Mean'].mean()
Year = pd.DatetimeIndex(CA_Pollution['Date Local']).year

plt.plot(AveragePollution)