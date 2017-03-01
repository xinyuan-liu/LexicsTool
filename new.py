#!/usr/local/bin/python3
import pickle
class Item:
    root=''
    meaning=''
    example=''
    def print(self):
        print(self.root)
        print(self.meaning)
        print(self.example)
db=pickle.load(open('db.pkl','rb'))
index=pickle.load(open('index.pkl','rb'))
letter=input('letter:')
import readchar
for i in index[letter]:
    db[i].print()
    key=readchar.readchar()
    if ord(key)==3:
        exit()
