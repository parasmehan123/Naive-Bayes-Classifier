import pandas as pd
import numpy as np

d1=pd.read_csv('data1',sep=' ',header=None)
d2=pd.read_csv('data2',sep=' ',header=None)
d3=pd.read_csv('data3',sep=' ',header=None)

d1.drop(0,axis=1,inplace=True)
d1.drop(8,axis=1,inplace=True)
d2.drop(0,axis=1,inplace=True)
d2.drop(8,axis=1,inplace=True)
d3.drop(0,axis=1,inplace=True)
d3.drop(8,axis=1,inplace=True)

data1=d1.to_numpy()
data2=d2.to_numpy()
data3=d3.to_numpy()

d1_c0={1:np.array([0,0,0]),2:np.array([0,0,0]),3:np.array([0,0]),4:np.array([0,0,0]),5:np.array([0,0,0,0]),6:np.array([0,0])}
d1_c1={1:np.array([0,0,0]),2:np.array([0,0,0]),3:np.array([0,0]),4:np.array([0,0,0]),5:np.array([0,0,0,0]),6:np.array([0,0])}
d1_c=0 # counts no of 1
d2_c0={1:np.array([0,0,0]),2:np.array([0,0,0]),3:np.array([0,0]),4:np.array([0,0,0]),5:np.array([0,0,0,0]),6:np.array([0,0])}
d2_c1={1:np.array([0,0,0]),2:np.array([0,0,0]),3:np.array([0,0]),4:np.array([0,0,0]),5:np.array([0,0,0,0]),6:np.array([0,0])}
d2_c=0 # counts no of 1
d3_c0={1:np.array([0,0,0]),2:np.array([0,0,0]),3:np.array([0,0]),4:np.array([0,0,0]),5:np.array([0,0,0,0]),6:np.array([0,0])}
d3_c1={1:np.array([0,0,0]),2:np.array([0,0,0]),3:np.array([0,0]),4:np.array([0,0,0]),5:np.array([0,0,0,0]),6:np.array([0,0])}
d3_c=0 # counts no of 1

for i in data1:
    for j in range(1,len(i)):
        if i[0]==0:
            d1_c0[j][i[j]-1]+=1
            
        else:
            d1_c1[j][i[j]-1]+=1
    if i[0]==1:
        d1_c+=1

for i in data2:
    for j in range(1,len(i)):
        if i[0]==0:
            d2_c0[j][i[j]-1]+=1
            
        else:
            d2_c1[j][i[j]-1]+=1
    if i[0]==1:
        d2_c+=1
    
for i in data3:
    for j in range(1,len(i)):
        if i[0]==0:
            d3_c0[j][i[j]-1]+=1
            
        else:
            d3_c1[j][i[j]-1]+=1
    if i[0]==1:
        d3_c+=1
    
for i in d1_c0.keys():
    d1_c0[i]=d1_c0[i]/(len(data1)-d1_c)
    d1_c1[i]=d1_c1[i]/d1_c
    d2_c0[i]=d2_c0[i]/(len(data2)-d2_c)
    d2_c1[i]=d2_c1[i]/d2_c
    d3_c0[i]=d3_c0[i]/(len(data3)-d3_c)
    d3_c1[i]=d3_c1[i]/d3_c

def pred1(x):
    p0=1
    p1=1
    global d1_c0,d1_c1
    for i in range(1,len(x)):
        p0*=d1_c0[i][x[i]-1]
        p1*=d1_c1[i][x[i]-1]
        
    if p0>p1:
        return 0
    else :
        return 1

def pred2(x):
    p0=1
    p1=1
    global d2_c0,d2_c1
    for i in range(1,len(x)):
        p0*=d2_c0[i][x[i]-1]
        p1*=d2_c1[i][x[i]-1]
        
    if p0>p1:
        return 0
    else :
        return 1
    
def pred3(x):
    p0=1
    p1=1
    global d3_c0,d3_c1
    for i in range(1,len(x)):
        p0*=d3_c0[i][x[i]-1]
        p1*=d3_c1[i][x[i]-1]
        
    if p0>p1:
        return 0
    else :
        return 1

t1=pd.read_csv('test1',sep=' ',header=None)
t2=pd.read_csv('test2',sep=' ',header=None)
t3=pd.read_csv('test3',sep=' ',header=None)
t1.drop(0,axis=1,inplace=True)
t1.drop(8,axis=1,inplace=True)
t2.drop(0,axis=1,inplace=True)
t2.drop(8,axis=1,inplace=True)
t3.drop(0,axis=1,inplace=True)
t3.drop(8,axis=1,inplace=True)
test1=t1.to_numpy()
test2=t2.to_numpy()
test3=t3.to_numpy()

ac=0
for i in test1:
    if i[0]==pred1(i):
        ac+=1
for i in test2:
    if i[0]==pred2(i):
        ac+=1
for i in test3:
    if i[0]==pred3(i):
        ac+=1
        
file=open('../Answers.txt','a')
file.write("\nMonk :"+str(ac/(len(test1)+len(test2)+len(test3))))