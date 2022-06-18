'''3.Identity Matrix'''
import numpy as np
dimension = int(input("Enter dimension of identitiy matrix: "))
identity_matrix = np.identity(dimension, dtype="int")
print(identity_matrix)