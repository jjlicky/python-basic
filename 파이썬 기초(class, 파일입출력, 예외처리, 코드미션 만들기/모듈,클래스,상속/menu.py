import sauce as s
import meat as m
import sys

class Menu:
    def 소불고기(self,n):
        self.n=n
        print("메뉴명 : 소불고기")
        m.beef()
        m.gram(n)
        s.soy()
    def 제육볶음(self,n):
        self.n=n
        print("메뉴명 : 제육볶음")
        m.pork()
        m.gram(n)
        s.spicy()
    def 닭볶음탕(self,n):
        self.n=n
        print("메뉴명 : 닭볶음탕")
        m.chicken()
        m.gram(n)
        s.spicy()

class MenuForKids(Menu):
    def 닭볶음탕(self,n):
        self.n=n
        print("메뉴명 : 닭볶음탕")
        m.chicken()
        m.gram(n)
        s.soy()     #오버라이딩 (맵지않게 소스바꿈)

def say(day):
    print("-------")
    print(day+"점심메뉴안내:")
    print("다음 재료를 준비하세요.")

lunch_monday = Menu()
lunch_tuesday = Menu()
lunch_wednesday = MenuForKids()

f=open("메뉴개발결과.txt",'w')
stdout=sys.stdout
sys.stdout=f

say("월요일")
lunch_monday.소불고기("1200")

say("수요일")
lunch_wednesday.닭볶음탕("600")

f.close()
sys.stdout=stdout
