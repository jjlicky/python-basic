lst=[]
for i in range(0,4):
    lst.append(0)

sum=0
for i in range(0,4):
    lst[i] = int(input(str(i+1)+"번째 숫자 입력:"))
for i in range(0,4):
    sum = sum + lst[i]
print("합계 %d" %sum)
