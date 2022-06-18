'''Question-1
Consider the vector [10, 11, 12, 13, 14], how to build a new vector with 5 consecutive zeros interleaved between each value?
Sample Input
First Number: 10
Last Number: 14
Sample Output
[10.  0.  0.  0.  0.  0. 11.  0.  0.  0.  0.  0. 12.  0.  0.  0.  0.  0. 13.  0.  0.  0.  0.  0. 14.]'''
import numpy as np
arr = []
a = int(input("Size of array:"))
for i in range(a):
    arr.append(float(input("\nEnter element:")))
my_array = np.array(arr)
print(np.floor(arr))
l = 5
new_arr = np.zeros(len(arr) + (len(arr)-1)*(l))
new_arr[::l+1] = arr
print("\nNew array:")
print(new_arr)