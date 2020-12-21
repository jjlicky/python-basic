def order(num):
    print("주문하실 음료를 입력하세요:")
    drink=input()
    return drink
num=2
drink=order(num)
print("주문하신 {}가 {}개 완료되었습니다.".format(drink,num))
