#!/usr/local/bin/python3
import pickle
status=pickle.load(open('status.pkl','rb'))
print(status)
cntripe=0
cntraw=0
for i in status:
    if i==-1:
        cntripe+=1
    elif i>0:
        cntraw+=1
print('-1:'+str(cntripe)+'\traw:'+str(cntraw)+'\ttotal:'+str(cntripe+cntraw))
