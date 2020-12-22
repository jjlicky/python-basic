from turtle import*

shape("turtle")

i=1


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
    if i%3==2:
        color("red", "red")
        begin_fill()
        rectangle()
        end_fill()
    elif i%3==0:
        color("red", "yellow")
        begin_fill()
        triangle()
        end_fill()
    elif i%3==1:
        color("red", "blue")
        begin_fill()
        circle(100)
        end_fill()

    left(10)
    i+=1
end_fill()
