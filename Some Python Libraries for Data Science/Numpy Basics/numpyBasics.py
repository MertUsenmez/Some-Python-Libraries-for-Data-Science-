# -*- coding: utf-8 -*-
"""

@author: User
"""

 #%% Numpy
 
 import numpy as np
 
 array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])  #1*15 matrix(vector)
 
 print(array.shape)
 
 a = array.reshape(3,5)
 
 print("Shape:",a.shape)
 
 print("Dimension:",a.ndim)
 
 print("Data type:",a.dtype.name)
 
 print("Size:",a.size)
 
 print(type(a))
 
 array1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
 
 
 zeros = np.zeros((3,4))    # memory allocation
 
 zeros[0,0]=5
 print(zeros)
 zeros[2,3]=8
 print(zeros)

 np.ones((3,4))

np.empty((3,2))

 a = np.arange(10,50,5)  # From 10 until 50, +5 a array of increasing.
 print(a)
 
 a = np.linspace(5,50,20)   # Print 20 numbers between 5 and 50.
 print(a)
 
 #%%
 
 #%% Numpy Basic Operations
 
 
 a = np.array([1,2,3])
 b = np.array([3,4,5])
 
 print(a+b)
 print(a-b)
 print(a**2)
 
 print(np.sin(a))
 
 print(a<2)
 
 
 
 a = np.array([[1,2,3],[4,5,6]])
 b = np.array([[1,2,3],[4,5,6]])
 
 # Element wise product.
 print(a*b)
 
 # Matrix product.
 print(a.dot(b.T))  #b.T b'nin transpozudur.
 
 # Exponential of a.
 print(np.exp(a))
 
 # Creates a random matrix(5x5) of numbers between 0 to 1.
 a = np.random.random((5,5))
 
 print(a.sum())
 print(a.max())
 print(a.min())
 
 # sum of columns
 print(a.sum(axis=0))
 
 # sum of rows
 print(a.sum(axis=1))
 
 # square root
 print(np.sqrt(a))
 
 # squared
 print(a**2)
 
 print(np.add(a,a))


 #%% Shape Manipulation
 
 array = np.array([[1,2,3],[4,5,6],[7,8,9]])  # 3x3 matrix
 
 # Let's turn this matrix into a vector, that is, to a 1-dimensional array.
 # flatten
 a = array.ravel()
 
 # we want to make a 3-dimensional array again.
 array2 = a.reshape(3,3)
 
 # Transpose of array2
 arrayT = array2.T
 print(arrayT)
 
 print(arrayT.shape)
 

 #%% stacking array
 
 array1 = np.array([[1,2],[3,4]])
 array2 = np.array([[-1,-2],[-3,-4]])
 
 # arrays(matrix) horizontal merge
 array3 = np.hstack((array1,array2))
 
 # arrays(matrix) vertical merge
 array4 = np.vstack((array1,array2))
 
 
 #%% convert array and copy array
 
 # convert
 liste = [1,2,3,4]
 print(type(liste))
 
 array1 = np.array(liste)
 print(type(array1))
 
 liste1 = list(array1)
 
 # copy
 a = np.array([1,2,3,4])
 
 b = a
 c = a
 
 b[0] = 5 # In this case, a, b, c will change because those are kept as an area in memory. Those are not kept as a value in memory.
 
 # If we want no change those.
 d = np.array([1,2,3,4])
 
 e = d.copy()
 f = d.copy()
 # Using the copy() method, we created new fields for e and d so that the changes do not depend on each other.
 
 e[0] = 5
 
 
 
 
 
 
 