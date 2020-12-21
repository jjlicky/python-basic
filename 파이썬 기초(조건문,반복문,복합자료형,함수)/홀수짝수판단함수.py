def odd_or_even(num):
    if num%2 == 0:
       return "even"
    else:
       return "odd"

num=int(input("숫자를 입력하세요:"))
print(odd_or_even(num))
