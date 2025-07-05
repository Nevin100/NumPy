#Stacking :

'''horizontal Stacking : --> hstack()'''
'''vertical Stacking : --> vstack()'''

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print("Vertical Stacking :",np.vstack((arr1,arr2)))
print("Horizontal Stacking :",np.hstack((arr1,arr2)))
