# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:23 2024

@author: user
"""

"""
Storing data in Python
1. Lists
2. Dictionaries
3. Data Frames - specific to pandas
"""

import pandas

file = pandas.read_csv("country_data.csv")

print(file)

age1 = 30
age2 = 25
age3 = 29

age = [30,25,29,46,22]

print(age)

print(age[0])

print(age[1])

print(min(age))

print(max(age))

print(sum(age))

print(len(age))

avg = sum(age)/len(age)

print(avg)

g1 = "M"
g2 = "F"
g3 = "M"

gender = ["M","F","F"]

c1 = "South Africa"
c2 = "Lesotho"

print(age[0:2])

age.append(100)

print(age)

names = ["A","B","C"]

#file = pandas.read_csv("housing data")

print(age)
age.insert(0,100)

"""
Dictionaries - key:value pairs

cat: "a cute animal"

- unordered

"""


mammals = {"cat":"a cute animal","lion":"king of the jungle","elephant":"a gigantic herbivore"}

print(mammals["cat"])

print(mammals["lion"])

print(mammals["elephant"])


"""
Data Frames
"""

fruits = ["apple","banana","orange","grape","kiwi"]

size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
    'fruits': fruits,
    'sizes':size_nm
    }

"""
df = dataframe
"""

import pandas as pd

df = pd.DataFrame(fruit_sizes)

print(df['fruits'])

print(df['sizes'])

print(df['sizes'].min())

print(df['sizes'].mean())

print(df.describe())

print(df[df["sizes"] >10])

print(df[1:3])

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices

df.drop(columns=["sizes"], inplace=True)







