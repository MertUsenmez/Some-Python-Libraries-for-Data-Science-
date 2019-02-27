# -*- coding: utf-8 -*-
"""

@author: User
"""
 
# matplotlib library
# data visualization library
# line plot, scatter plot, bar plot, subplots, histogram

# We will visualize the iris data, but first we will put the iris data into a dataframe to see what's in it.

#%%
import pandas as pd

df = pd.read_csv("iris.csv")

# features
print(df.columns)

# return unique rows of species column
print(df.Species.unique())

print(df.info())

print(df.describe())

# We split the Setosa ones into a separate dataframe.
setosa = df[df.Species == "Iris-setosa"]

# We split the Versicolor ones into a separate dataframe.
versicolor = df[df.Species == "Iris-versicolor"]

print(setosa.describe())
print(versicolor.describe())

#%%   line plot

import matplotlib.pyplot as plt

# delete id column of df and create a new dataframe(This dataframe name is df1) add the Id in this dataframe.
df1 = df.drop(["Id"], axis=1)

df1.plot()
plt.show()

# Separate into separate dataframes and visualize one by one.
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id, setosa.PetalLengthCm, color="red", label='setosa ')
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color="green", label='versicolor ')
plt.plot(virginica.Id, virginica.PetalLengthCm, color="blue", label='virginica ')
plt.xlabel("ID")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()

df1.plot(grid=True, alpha=1)
plt.show()

#%%   scatter plot -- Unlike line plot, it is used to compare two things more.

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.Id, setosa.PetalLengthCm, color="red", label='setosa ')
plt.scatter(versicolor.Id, versicolor.PetalLengthCm, color="green", label='versicolor ')
plt.scatter(virginica.Id, virginica.PetalLengthCm, color="blue", label='virginica ')
plt.legend()
plt.title("Scatter Plot")
plt.xlabel("ID")
plt.ylabel("PetalLengthCm")
plt.show()

#%%  Histogram is an important representation that shows frequencies.

plt.hist(setosa.PetalLengthCm, bins=20)
plt.xlabel("Cm Of Records")
plt.ylabel("Frekans Of Records")
plt.title("Histogram")
plt.show()

#%% bar plot

import numpy as np

x = np.array([12,10,30,40,21,35])
a = ["TURKEY", "GEORGIA", "GERMANY", "ENGLAND", "NORWAY", "USA"]
y = x*2+5

plt.bar(a,y)
plt.title("Bar Plot")
plt.xlabel("Countries")
plt.ylabel("Per Capita Income")
plt.show()

#%% sub plots


setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

# 1.row 1.column
plt.subplot(2,1,1)
plt.plot(setosa.Id, setosa.PetalLengthCm, color="red", label='setosa ')
plt.ylabel("setosa - PetalLengthCm")

# 1.row 2.column
plt.subplot(2,1,2)
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color="green", label='versicolor ')
plt.ylabel("versicolor - PetalLengthCm")

plt.show()






