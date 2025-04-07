import random 
list=[]
for i in range(0,5):
    number=random.randint(-6,10)
    list.append(number)
    i=i+1
print(list)
s=0
for i in list:
    if i>0:
        s=s+i
print(s)
