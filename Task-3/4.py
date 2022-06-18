'''Question-4
Convert the first character of each element in a series to uppercase?
Sample Input
ser = pd.Series(['amrita', 'school', 'of', 'engineering' 'chennai' , 'campus'])
Sample Output
Amrita School Of Engineering Chennai Campus'''
import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering' 'chennai' , 'campus'])
#ser = pd.Series(input("Enter String: "))
print("Original Series:")
print(ser)
result = ser.map(lambda x: x[0].upper() + x[1:-1] + x[-1])
for i in result:
    print(i,end=' ')