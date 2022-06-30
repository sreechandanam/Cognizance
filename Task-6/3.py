'''3.Read the file 'about.txt' and find the words with atleast 6 letters and the most frequently used word.
Contents of the file 'about.txt':
Python has tools for almost every aspect of scientific computing. The Bank of America uses Python to crunch its financial data and Facebook looks upon the Python library Pandas for its data analysis. 
While there are many libraries available to perform data analysis in Python, here are a few: NumPy, SciPy, Pandas and Matplotlib.'''
count = 0
word = ""
max_count = 0 
words = [] 
file = open("about.txt","r")  
for line in file:  
    string = line.lower().replace(',','').replace('.','').split(" ")
    for s in string: 
        if len(s) == 6:
            words.append(s);    
for i in range(0, len(words)):  
    count = 1
    for j in range(i+1, len(words)):  
        if(words[i] == words[j]):  
            count = count + 1            
    if(count > max_count):  
        max_count = count
        word = words[i]         
print("Most repeated word:" + word)
file.close()