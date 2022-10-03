import csv
data1=[]
data2=[]
with open("final1.csv","r") as f:
    reading=csv.reader(f)
    for i in reading:
        data1.append(i)

with open("arc.csv","r") as g:
    reading=csv.reader(g)
    for i in reading:
        data2.append(i)

header1=data1[0]
planetdata1=data1[1:]

header2=data2[0]
planetdata2=data2[1:]


header=header1+header2
data=[]
for i,j in enumerate(data1):
    data.append(data1[i]+data2[i])

with open("merge.csv",'a+') as a:
    writing=csv.writer(a)
    writing.writerow(header)
    writing.writerows(data)
