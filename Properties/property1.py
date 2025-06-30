#  Shape , Size, Ndim, Datatype of an array

import numpy as np
arr_2d = np.array([[1,2,3],[4,5,6]])

print("Shape :", arr_2d.shape) #-- > (2,3) : Number of rows : 2 and Number of Colunms : 3

#Size of array :
print("Size :", arr_2d.size) #--> 6 (Number of Elements in the array)

#Dimmensions of array :
print("Dimmendion (1D/2D/3D ..) :", arr_2d.ndim) # --> 2 (Dimmension of the array )

#Datatype of an array :
print("Datatype of an array :", arr_2d.dtype) # --> Int64 (Datatype of array)