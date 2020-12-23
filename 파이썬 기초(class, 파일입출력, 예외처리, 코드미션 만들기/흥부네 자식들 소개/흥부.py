class Father:
    def nose(self):
        print('아빠처럼 코가 주먹코입니다.')
    def eyes(self):
        print('아빠를 닮아 눈이 작습니다.')
    def mouse(self):
        print('아빠를 닮아 돌출형입니다.')

class Mother:
    def height(self):
        print("엄마를 닮아 키가 큽니다.")
    def eyes(self):
        print("엄마를 닮아 눈이 큽니다.")

class Son(Father):
    def say(self):
        print("안녕하세요.")
    def mouse(self):
        print("아빠를 닮지않아 돌출형이 아닙니다.")

class Daughter(Mother):
    def say(self):
        print("안녕하세요.")


#인스턴스 생성
son1 = Son()
son2 = Son()
son3 = Son()
daughter4 = Daughter()
daughter5 = Daughter()

#소개하기
print('[첫째아들 소개]')
son1.say()
son1.nose()
son1.mouse()

print('\n[둘째아들 소개]')
son2.say()
son2.nose()
son2.eyes()
son2.mouse()


print('\n[셋째아들 소개]')
son3.say()
son3.nose()
son3.mouse()

print('\n[넷째딸 소개]')
daughter4.say()
daughter4.height()

print('\n[다섯째딸 소개]')
daughter5.say()
daughter5.height()
daughter5.eyes()
