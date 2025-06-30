# Insetion of an element in an array :

#Syntax : np.insert(array, index, value, axis=None)

  # array : Inital Array
  # index : Position
  # value : value / literal to bve inserted
  # axis : for 1d--> its None for flatten, {for 2d--> (if 0: row-wise insertion) and (for 1: colunm-wise insertion)}

import numpy as np

arr = np.array([10,20,30,40,50])

print("Before Insertion :", arr)

new_arr = np.insert(arr, 1, 60, axis=None)
print("After Insertion :",new_arr)

# for 2d array : 
arr_2d = np.array([[10,20],[30,40]])
print("Original 2d Array :\n", arr_2d)

new_arr_2d = np.insert(arr_2d, 2, 80, axis=0) #--> row wise insertion
print("After Insertion 2D Array(RW):\n",new_arr_2d)

new_arr_2dd = np.insert(arr_2d, 2, 80, axis=1) #--> col wise insertion
print("After Insertion 2D Array(CW):\n",new_arr_2dd)
