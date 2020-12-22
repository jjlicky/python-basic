from turtle import*

shape("turtle")

i=1
color("red", "yellow")

def rectangle():
    n=1
    while n<5:
        forward(100)
        left(90)
        n+=1

def triangle():
    n2=1
    while n2<4:
        forward(100)
        left(120)
        n2+=1

begin_fill()
while i<37:
    if i%3==1:
        rectangle()
    elif i%3==2:
        triangle()
    elif i%3==0:
        circle(100)

    left(10)
    i+=1
end_fill()
