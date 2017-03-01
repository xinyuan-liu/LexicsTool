import pickle
status=[]
for i in range(550):
    status.append(0)
pickle.dump(status,open('status.pkl','wb'))

