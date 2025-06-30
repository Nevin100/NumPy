# Slicing : [start : stop: step]
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

#Slicing : [1:5] --> if no step provided, default step size : -1
print("Slicing from 2nd Element to 5th Elment :", arr[1:5]) #--> [2,3,4,5]

#Slicing : [4:9:2] 
print("Slicing with step size :", arr[4:9:2]) #--> [5,7,9]
