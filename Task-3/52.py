'''2.Multiplying a matrix'''
import numpy as np
print("Enter order of 1st matrix: ")
m,n = list(map(int,input().split()))
print("Enter Row wise values: ")
mat1 = []
for i in range(m) :
    print("Enter row",i,"value: ")
    row = list(map(int,input().split()))
    mat1.append(row)
print("Enter order of 2nd matrix: ")
p,q = list(map(int,input().split()))
print("Enter Row wise values: ")
mat2 = []
for j in range(p) :
    print("Enter row",j,"value:")
    row = list(map(int,input().split()))
    mat2.append(row)
print("Matrix 1: ",mat1)
print("Matrix 2: ",mat2)
print("Matrix Multiplication: ")
resultant = np.dot(mat1,mat2)
for row in resultant:
    print(row)