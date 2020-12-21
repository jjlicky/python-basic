def order():
    print("주문하실 음료를 입력하세요:")
    drink=input()
    return drink

drink=order()
print("주문하신 %s가 완료되었습니다."%drink)
