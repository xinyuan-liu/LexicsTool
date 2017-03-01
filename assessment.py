#!/usr/local/bin/python3
import pickle
import readchar
class Item:
    root=''
    meaning=''
    example=''
    def print(self):
        print(self.root)
        print(self.meaning)
        print(self.example)
f=open('db.pkl','rb')
db=pickle.load(f)
f.close()
index=pickle.load(open('index.pkl','rb'))
f=open('status.pkl','rb')
status=pickle.load(f)
f.close()
raw=[]
for i in range(len(status)):
    if status[i]>0:
        raw.append(i)

Range=input('Range:')
def changestatus(i):
    while True:
        key=readchar.readchar()
        if key=='w':
            status[i]=3
            break
        elif key=='q':
            if status[i]==1:
                status[i]=-1
            elif status[i]!=-1:
                status[i]=status[i]-1
            break
if Range in index:
    Range=index[Range]
elif Range=='raw':
    Range=raw    
import random
random.shuffle(Range)
for i in Range:
    print(db[i].root)
    while True:
        key=readchar.readchar()
        if key=='1':
            print(db[i].meaning)
            readchar.readchar()
            print(db[i].example)
            changestatus(i)
            break
        elif key=='2':
            print(db[i].example.strip())
            readchar.readchar()
            print(db[i].meaning+'\n')
            changestatus(i)
            break
        else:
            if ord(key)==3:
                pickle.dump(status,open('status.pkl','wb'))
                exit()
pickle.dump(status,open('status.pkl','wb'))
