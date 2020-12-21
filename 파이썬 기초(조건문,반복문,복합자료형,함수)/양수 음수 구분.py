
for i in range(27):
    print("=",end="")
print()
a=int(input("정수를 입력하세요(1~100):"))
if a>0:
    print("양수입니다.")
elif a<0:
    print("음수입니다.")
else:
    print("0입니다.")
