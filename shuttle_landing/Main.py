
import pandas as pd
import numpy as np
from copy import deepcopy as dp

d=pd.read_csv('data',sep=',',header=None).to_numpy()

def pred(x,y):
    xt=x.transpose()
    d1={}
    for i in range(1,len(xt)):
        d1[i]={}
        for j in xt[i]:
            if j!='*' and j not in d1[i].keys():
                d1[i][j]=0
    #print(d1)
           
    d2=dp(d1)
    c=[0,0]
    #print(d1,c)
    
    for i in x:
        if i[0]==1:
            c[0]+=1
            for j in range(1,len(i)):
                #print(j,i[j])
                if i[j]!='*':
                    d1[j][i[j]]+=1
                
        else:
            c[1]+=1
            for j in range(1,len(i)):
                if i[j]!='*':
                    d2[j][i[j]]+=1
        
    #print(d1,d2,sep="\n")
    
    for i in d1.keys():
        for j in d1[i].keys():
            d1[i][j]=d1[i][j]/c[0]
            
    for i in d2.keys():
        for j in d2[i].keys():
            d2[i][j]=d2[i][j]/c[1]
       
    #print(d1,d2,sep='\n')
    
    p=[1,1]
    for i in range(1,len(y)):
        if y[i]!='*':
            if y[i] in d1[i].keys():
                p[0]*=d1[i][y[i]]
            else:
                p[0]=0
            if y[i] in d2[i].keys():
                p[1]*=d2[i][y[i]]
            else:
                p[1]=0
    
    z=p.index(max(p))
    if z==0:
        return 1
    else:
        return 2
    
ac=0
for i in range(len(d)):
    #print(d[i])
    if d[i][0]==pred(np.vstack((d[:i],d[i+1:])),d[i]):
        ac+=1

file=open('../Answers.txt','a')
file.write("\nShuttle Landing :"+str(ac/len(d)))