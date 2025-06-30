#Reshaping : reshape(rows, cols) 
#Note : No Copy is generated , it affects the original or the inital array

import numpy as np

arr = np.array([10,20,30,40,50,60])

reshape_Array = arr.reshape(2,3)

print("Original Array :", arr)
print("Reshaped Array : \n", reshape_Array)
