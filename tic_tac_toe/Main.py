import pandas as pd
import numpy as np
from copy import deepcopy as dp

d=pd.read_csv('data',sep=',',header=None).to_numpy()

def pred(x,y):
    xt=x.transpose()
    d1={}
    for i in range(len(xt)-1):
        d1[i]={}
        for j in xt[i]:
            if j not in d1[i].keys():
                d1[i][j]=0
             
    d2=dp(d1)
    c=[0,0]
    #print(d1,c)
    
    for i in x:
        if i[-1]=='positive':
            c[0]+=1
            for j in range(len(i)-1):
                #print(j,i[j])
                d1[j][i[j]]+=1
                
        else:
            c[1]+=1
            for j in range(len(i)-1):
                d2[j][i[j]]+=1
        
        
    for i in d1.keys():
        for j in d1[i].keys():
            d1[i][j]=d1[i][j]/c[0]
            
    for i in d2.keys():
        for j in d2[i].keys():
            d2[i][j]=d2[i][j]/c[1]
       
    #print(d1,d2,sep='\n')
    p=[1,1]
    for i in range(len(y)-1):
        p[0]*=d1[i][y[i]]
        p[1]*=d2[i][y[i]]
    
    z=p.index(max(p))
    if z==0:
        return 'positive'
    else:
        return 'negative'
    
ac=0
for i in range(len(d)):
    if d[i][-1]==pred(np.vstack((d[:i],d[i+1:])),d[i]):
        ac+=1

file=open('../Answers.txt','a')
file.write("\nTic Tac Toe :"+str(ac/len(d)))
    
