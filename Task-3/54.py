'''4.Array datatype conversion'''
import numpy as np
arr = []
a = int(input("Size of array: "))
for i in range(a):
    arr.append(float(input("Element: ")))
arr = np.array(arr)
print(np.floor(arr))