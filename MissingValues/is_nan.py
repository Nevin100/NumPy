#Missing Value : 1.) isnan()

import numpy as np

arr = np.array([1,2,np.nan,4,np.nan])

print("check missing values :", np.isnan(arr))