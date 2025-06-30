#Fancy Indexing : multiple indexs at once [.., .., ..]

import numpy as np

arr = np.array([10,20,30,40,50])

print("Multiple Index position values Retreived at once",arr[[0,2,4]]) #-->[ 10 30 50 ]