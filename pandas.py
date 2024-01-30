# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:13:01 2024

@author: user
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

print(file.info())

print(file.describe())

file = pandas.read_csv("iris.csv")

print(file)

print(file.info())

print (file.describe())

file  = pandas.read_csv("insurance_data.csv",skiprows=5)

print(file)

file = pandas.read_csv("diab_data.csv")

print(file)

file = pandas.read_csv("housing_data.csv")

print(file)

#column_names = ["A", "B", "C"....]

#file = pandas.read_csv("housing_data.csv", names = column_names)

#file = pandas.read_csv("Geospatial Data.txt",sep=";")
#print(file)
#print(file.info())








