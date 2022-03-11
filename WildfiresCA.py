#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 09:39:46 2022

@author: ekaumsoni
"""

import pandas as pd
import matplotlib as plt

#Convert CSV to Dataframe
Wildfires_DF = pd.read_csv('Wildfires.csv')
Weather_DF = pd.read_csv('CaliforniaWeather.csv')

# Wildfires per year
FiresPerYear = Wildfires_DF.groupby(['YEAR_']).count()
FiresPerYear['OBJECTID'].plot()


#Size of Wildfire


#Average Size
# Most common of Wildfires