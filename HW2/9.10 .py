import csv
freq={}
filename=input()
with open(filename, 'r') as csv_file:
    csvreader = csv.reader(csv_file)
    line=next(csvreader)
    for word in line:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
for i in freq:
    print(i, freq[i])