from turtle import*

shape("turtle")

n=0
n2=1
length=100

while n2<11:
    if n2%2==0:
        length = 50
    else:
        length = 100
    
    while n<4:
        forward(length)
        left(90)
        n+=1
    n=0
    left(36)
    n2+=1
