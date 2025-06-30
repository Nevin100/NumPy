# Creation of array :
import numpy as np
arr = np.array([1,2,3])

# with default 0 values :
arr = np.zeros(3)

# with defualt 1 values :
arr = np.ones(4)

arr = np.ones((2,3)) #--> shape
print(arr)

#full fn -> (shape, values)
filled_array = np.full((2,2),7)
print(filled_array)
