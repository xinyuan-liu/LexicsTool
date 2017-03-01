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
    if status[i]==3:
        raw.append(i)
import random
random.shuffle(raw)
import readchar
for i in raw:
    db[i].print()
    key=readchar.readchar()
    if ord(key)==3:
        exit()

