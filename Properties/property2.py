# type Conversion of Elements :
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])
print("Original Type :",arr.dtype)

float_arr = arr.astype(float)
print("New type :", float_arr.dtype)