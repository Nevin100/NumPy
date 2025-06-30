# Insert an element at the end : append(original_arr, values_to_be_append)

import numpy as np

arr = np.array([10,20,30,40,50])

new_arr = np.append(arr, [60,70,80])
print("After Appending : ", new_arr)


# Concatenation : Addition of 2 arrays
arr1 = np.array([10,20,30])
arr2 = np.array([40,50,60])

arr3 = np.concatenate(arr1,arr2) #-for 2d : axis is also given-> if 0=> Vertical Stacking, if 1=> horizontal Stacking
print("Concatenation :", arr3)
