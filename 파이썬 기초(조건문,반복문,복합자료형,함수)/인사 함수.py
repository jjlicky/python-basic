def message(m):
    if m=='happy':
        print("행복하세요")
    elif m=='sad':
        print("힘내세요")
def name(n):
    print("%s님, 안녕하세요."%n)
    feel=input("오늘 기분어떠신가요? (happy or sad):")
    message(feel)

myname=input("이름을 입력해주세요 :")
name(myname)
