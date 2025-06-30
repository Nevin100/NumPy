#Deletion of element --> np.delete(arr, position, axis=None)

import numpy as np

arr = np.array([10,20,30,40,50])
print("Initial Array :", arr)

new_arr = np.delete(arr, 2)
print("New Array :", new_arr)

