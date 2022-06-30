'''1. Write a python program that reads the contents from the given file "onelinefile.txt". The file contains a single line which is of the format (int)(string)(float)(string) repeatedly. For e.g.
1Aaa3.5Maths2Bbb4.2Physics3Ccc7.62Chemistry
Your main task is to split the contents of the given file based on their format and write it into a .csv file say "Filename2.csv". For e.g. the above txt file should be converted into a csv file such that the contents look like this:
1,Aaa,3.5,Maths
2,Bbb,4.2,Physics
3,Ccc,7.62,Chemistry
Contents of "onelinefile.txt"
1Aaa3.5Maths2Bbb4.2Physics3Ccc7.62Chemistry4Ddd9.55Biology5Eee4.0Social6Fff7.6English7Ggg3.111Maths8Hhh9.99Physics9Iii1.23Civics'''
import re,csv
f = open('onelinefile.txt')
for i in f:
        a = re.findall(r'[+-]?[0-9]+\.[0-9]+', i) 
        b = re.findall(r'[a-zA-Z]+', i)
        c = 0
        for p in range(len(a)):
            with open('onelinefile.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([str(p+1), b[c],a[p],b[c+1]])
            c += 2
with open('onelinefile.csv', 'r',) as file:
    reader = csv.reader(file)
    for row in reader:
        print(','.join(row))