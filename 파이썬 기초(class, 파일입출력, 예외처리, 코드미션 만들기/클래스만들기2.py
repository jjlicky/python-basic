import random

class Modoom:
    def choose_mission(self,a):
        self.a=a
        if a==1:
            print("퀴즈프로그램 만들기")
        elif a==2:
            print("미로탈출 게임 만들기")
        elif a==3:
            print("미니애니메이션 만들기")

team1 = Modoom()
team2 = Modoom()
team3 = Modoom()

a_list = [1,2,3]
random.shuffle(a_list)
print("teams1 미션 랜덤뽑기:",end='')
a=a_list.pop()
team1.choose_mission(a)

print("teams2 미션 랜덤뽑기:",end='')
a=a_list.pop()
team2.choose_mission(a)

print("teams3 미션 랜덤뽑기:",end='')
a=a_list.pop()
team3.choose_mission(a)
