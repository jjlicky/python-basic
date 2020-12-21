a = input("중단할 문자를 입력하시오.")

for b in 'strawberry':
    if b == a:
        continue            #돌고있던 루프 처음으로 돌아
    print(b, end="")
