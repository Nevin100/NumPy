# Broadcasting :

import numpy as np

prices = np.array([100,90,80,70,60])

discount = 10

final_Prices = prices - (prices * discount/100)

print("Final Prices :", final_Prices)