import random


y1=0
y2=0
y3=0
y4=0

def yoot():
    y1=random.randint(0,1)
    y2=random.randint(0,1)
    y3=random.randint(0,1)
    y4=random.randint(0,1)
    yoot1=[y1,y2,y3,y4]
    return yoot1

print(yoot())
