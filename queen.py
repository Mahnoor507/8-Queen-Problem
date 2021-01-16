#!/usr/bin/env python
# coding: utf-8

# In[456]:


from random import randint
import numpy as np
for j in range(8):
    k=randint(0,7)
    cl1[j]=k
for j in range(8):
    k=randint(0,7)
    cl2[j]=k
for j in range(8):
    k=randint(0,7)
    cl3[j]=k
for j in range(8):
    k=randint(0,7)
    cl4[j]=k  
#defining intial population of 4

#l containing 4 boards ... initial population

print(cl1,cl2,cl3,cl4) 

def fitnessfun(queen):
    count =0
    i=0
    #creating a board
    new=np.zeros((8,8),dtype=int)
    #placing queens on that bord
    for x in range(8):
        y=int(queen[x])
        new[y,x]=1
    for col in range(8):
        verticalchk=0;
        horizontalchk=0;
        fdiagonal=0;
        bdiagonal=0;
        row=queen[col];
        #horizontally checking queens
        for c in range(8):
            if(new[int(row),int(c)] == 1 and c != col):
                horizontalchk=1
        #vertically checking queens        
        for r in range(8):
            if(new[r,col] == 1 and r != row):
                verticalchk=1
        #forward diagonal queens
        frow = int(row)
        fcol = int(col)
        while (frow > 0 and fcol > 0):
            frow = frow - 1
            fcol = fcol - 1
        while (frow < 8 and fcol < 8):
            if(new[frow,fcol] == 1 and frow != row and fcol != col):
                fdiagonal=1
            frow = frow + 1
            fcol = fcol + 1
        #backward diagonal queens
        brow = int(row)
        bcol = int(col)
        while (brow > 0 and bcol < 7):
            brow = brow - 1
            bcol = bcol + 1
        while (brow < 8 and bcol >= 0):
            if(new[brow,bcol] == 1 and brow != row and bcol != col):
                bdiagonal=1
            brow = brow + 1
            bcol = bcol - 1
            
        if horizontalchk!=1 and verticalchk!=1 and fdiagonal!=1 and bdiagonal!=1 :
            count=count+1  
    #total no of fitness queens or fitness val of a board
    return count;    
    
#for counting iterations 
count=0    
 #list for holding boards
blue=[cl1,cl2,cl3,cl4]
print("Finding best possible solution")
flag=False;
while flag!=True:    
    #array for holding fitness valuess
    green=np.array([0,0,0,0])
    y=0;
    for x in blue:
        green[y]=fitnessfun(x)
        y=y+1
    #array for holding sorted fitness values
    red=np.array([0,0,0,0])
    t=green.copy()
    red=t
    red.sort()
    #success yayyy found solution
    if 8 in green:
        print("yayyyy solutionnnnnnnnnnnnnn")
        for i in range(4):
            k=green[i]
            if(k==8):
                print("Required solution is: ") 
                print(blue[i])
                print("Total no of iterations: ")
                print(count)
                hen=np.zeros((8,8),dtype=int)
                var=0
                for x in blue[i]:
                    hen[x,var]=1
                    var=var+1
                print("Board look like this")
                print(hen)
                flag=True
                break;
    #re arranging boardss
    for i in range(4):
        j=red[i]
        for b in range(4):
            h=green[b]
            if(h==j):
                temp[i]=blue[b]
    blue=temp
    #new arrays for working
    apple=mango=np.zeros(8,dtype=int)
    grapes=np.zeros(8,dtype=int)
    peach=np.zeros(8,dtype=int)
    #apple mango are parents best ones that kept 
    apple=blue[3];
    mango=blue[2];
    #crossover for new child
    for x in range(4):
        grapes[x]=apple[x]
        peach[x]=mango[x]      
    for x in range(4,8):
        grapes[x]=mango[x]
        peach[x]=apple[x]
    #mutation
    ran1=randint(0,7)
    while True:
        rn=randint(0,7)
        if grapes[ran1]!=rn:
            grapes[ran1]=rn
            break;

    ran2=random.randint(0,7)

    while True:
        rn=random.randint(0,7)
        if peach[ran2]!=rn:
            peach[ran2]=rn
            break;
    blue=[apple,mango,grapes,peach]
    count=count+1   
    if(count==10000):
        print("best possible solution in 10000 iterationss is: ")
        print(blue[3])
        print("The fitness is: ")
        print(red[3])
        hen=np.zeros((8,8),dtype=int)
        var=0
        for x in blue[3]:
            hen[x,var]=1
            var=var+1
        print("Board look like this")
        print(hen)
        flag=True;
        break; 

           


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




