# boolean Masking : filtering on the basis of condition 

import numpy as np

arr = np.array([10,20,30,40,50])

print("Elements greater than 20 :", arr[arr > 20]) #-->[30,40,50]

print("Elements smaller than 20 :", arr[arr < 20]) #-->[ 10 ]
