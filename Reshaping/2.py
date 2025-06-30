# ravel() --> View and flatten() --> Copy

import numpy as np

arr = np.array([[10,20],[30,40]])

#ravel()
print("ravel --> Views :", arr.ravel())

#flatten()
print("flatten --> Copy :", arr.flatten())