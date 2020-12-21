str = input("문자열을 입력:")

for i in range(len(str)-1,-1,-1):
    print("%c"%str[i],end="")
