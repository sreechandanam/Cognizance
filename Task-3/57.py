'''7.Getting the positions (indexes) where elements of 2 numpy arrays match'''
import numpy as np
a = np.array([0, 1, 2, 3, 4, 5, 6])
b = np.array([6, 5, 4, 3, 2, 1, 6])
c = np.where(a==b)
print(c)