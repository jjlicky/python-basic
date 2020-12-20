#입력된 금액만큼 동전을 500원, 100원, 50원, 10원짜리로 교환해주는 프로그램

money = int(input("교환할 금액을 입력하시오: "))

coin500 = money//500
money = money%500

coin100 = money//100
money = money%100

coin50 = money//50
money = money%50

coin10 = money//10
money = money%10

print("500원 %d개, 100원 %d개, 50원 %d개, 10원 %d개, \n바꾸지 못한 남은 잔액%d원" %(coin500, coin100, coin50, coin10, money))
