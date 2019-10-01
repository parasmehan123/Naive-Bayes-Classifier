import pandas as pd
import numpy as np
import csv

data=pd.read_csv('data_train',header=None).to_numpy()
count0=[0 for _ in range(23)]
count1=[0 for _ in range(23)]
count3=0

for i in data:
    if i[0]==1:
        count3+=1
        for j in range(1,len(i)):
            if i[j]==1:
                count1[j]+=1

    else:
        for j in range(1,len(i)):
            if i[j]==0:
                count0[j]+=1
                d={}

p=count3/(len(data))
d[0]=p
for i in range(1,23):
    d[i]=[count0[i]/count3,count1[i]/count3]

def pred(x):
    global d
    p0=1
    p1=1
    for i in range(1,len(x)):
        if x[i]==1:
            p0*=d[i][0]
            p1*=d[i][1]
        else:
            p0*=(1-d[i][0])
            p1*=(1-d[i][1])
            
    if p0>p1:
        return 0
    else :
        return 1

data_test=pd.read_csv('data_test',header=None).to_numpy()
ac=0
for i in data_test:
    if i[0]==pred(i):
        ac+=1

file=open('../Answers.txt','a')
file.write("\nSpect Heart :"+str(ac/len(data_test)))
    