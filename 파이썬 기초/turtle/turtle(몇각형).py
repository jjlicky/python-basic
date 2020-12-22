from turtle import*

print("몇각형을 그릴까요?")
answer = int(input())

i=0
while i < answer:
    forward(100)
    left(360/answer)
    i=i+1
