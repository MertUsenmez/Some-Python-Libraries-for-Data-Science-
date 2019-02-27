# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Why Pandas ? :
# 1) Fast and efficient for DataFrames.
# 2) Pandas library provides convenience for files between files. (Orn: .csv to .txt)
# 3) Makes our work easier from Missing Value Data.
# 4) We can reshape the data and use it more effectively.
# 5) Slicing and Indexing are easy in the Pandas Library.
# 6) Helps in Time Series Data analysis. (Time Series Data is functional (xy Coordinate) data).
# 7) Pandas is an optimized library of speed.

import pandas as pd

dictionary = {"Name":["Monalisa","Marlyn","Elizabeth","Maria","Lisa","Mert","Cristiano"], 
              "Surname":["Divano","Monro","Jueux","Salenero","Lohan","Usenmez","Ronaldo"], 
              "Age":[45,50,60,40,35,24,28]}

dataFrame1 = pd.DataFrame(dictionary)

head = dataFrame1.head()
tail = dataFrame1.tail()

head2 = dataFrame1.head(100)

#%% Pandas basic methods

# Return names of Features(Attributes).
print(dataFrame1.columns)

# Give us important information about DataFrame(DataSet).
print(dataFrame1.info())

# Return datatypes of Features(attributes).
print(dataFrame1.dtypes)

# Return and get only numeric features.
print(dataFrame1.describe())
# Output of describe()
# count : How many record?.
# mean : Avarage of this records.
# std : Standard Deviation.
# min : Minimum value.
# 25% : 1.quartile value.
# 50% : Median value.
# 75% : 3.quartile value.

#%%

print(dataFrame1["Age"])
print(dataFrame1.Age)

# Add new feature(column).
dataFrame1["new feature"] = [-1,-2,-3,-4,-5,-6,-7]

# Print type is not true because column name have a space character.  -> print(dataframe1.new feature)=?
# Using correct
print(dataFrame1["new feature"])

# Note: We should to avoid space character in feature names as posible.
# Take all rows, only print Age column.
print(dataFrame1.loc[:,"Age"])

# Take first three rows, only print Age column.
print(dataFrame1.loc[:3,"Age"])

print(dataFrame1.loc[:3,["Age","Name"]])

# Reverse
print(dataFrame1.loc[::-1,:])

print(dataFrame1.loc[:,:"Name"])

print(dataFrame1.iloc[:,2])

#%% filtering

import pandas as pd

# Describe dictionary
dictionary2 = {"Name":["Monalisa","Marly","Elizabeth","Maria","Lisa","Mert","Cristiano"], 
              "Surname":["Divano","Morro","Jueux","Salenero","Lohan","Usenmez","Ronaldo"], 
              "Age":[45,50,60,40,35,23,28],
              "Pay:":[4000, 5000, 3500, 2800, 4500, 12000, 15000]}

# Create DataFrame
dataFrame2 = pd.DataFrame(dictionary2)

# Filtering 
filter1 = dataFrame2.Age > 45

# Controlling type of filter = pandas.core.series.Series
type(filter1)

# Create a new dataframe from filtered data.
filtered_data = dataFrame2[filter1]

# Create a new filter.
filter2 = dataFrame2.Pay < 10000

# Merge two filter in the dataframe.
dataFrame2[filter1 & filter2]

print(dataFrame1[dataFrame1.Age > 40])



#%% List comprehension

import numpy as np

# Take average
average_age = dataFrame1.Age.mean()

dataFrame1["salary_level"] = ["low" if average_age > each else "high" for each in dataFrame1.Age]



#%% drop and concatenating

# For delete feature(attribute,column) from Dataframe.
dataFrame1.drop(["new feature"],axis=1,inplace=True)
# we can make with different way like this.
dataFrame1 = dataFrame1.drop(["new feature"],axis=1)

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

#Concatenation

# vertical
data_concat = pd.concat([data1,data2], axis=0)

# horizontal
name = dataFrame1.Name
surname = dataFrame1.Surname

data_h_concat = pd.concat([name,surname], axis=1)



#%% Transforming data

dataFrame1["list_comp"] = [each*2 for each in dataFrame1.Age]


# apply()
def multiply(age):
    return age*2

dataFrame1["apply_method"] = dataFrame1.Age.apply(multiply)













