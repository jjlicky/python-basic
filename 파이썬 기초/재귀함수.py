#재귀함수

def jumpRope(num):
    if(num<11):
        print("점프", num)
        num = num +1
        jumpRope(num)

jumpRope(1)
