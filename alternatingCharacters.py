prob = input ("please enter prob:")
prob = list(prob)
int (len(prob))
count=0
prv=0
nxt=1

while nxt < len(prob):
  if prob[prv]==prob[nxt]:
        del prob[nxt]
        count=count+1
  else:
        prv=prv+1
        nxt=nxt+1
        
print("A total of ", count, " item(s) have been deleted")
print(prob)

