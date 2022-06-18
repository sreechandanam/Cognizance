'''Question-2
Consider two random array A anb B, check if they are equal
Sample Input
First array:                                                           
[1 0 0 0 1 0]                                                          
Second array:                                                          
[0 0 1 1 0 1]
Sample Output
False'''
import numpy as np
a = np.random.randint(input("1st array:"))
# print("First array:")
# print(a)
b = np.random.randint(input("2nd array:"))
# print("Second array:")
# print(b)
array_equal = np.allclose(a,b)
print(array_equal)