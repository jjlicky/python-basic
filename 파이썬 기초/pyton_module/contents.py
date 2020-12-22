def inputinfo(month, date, place):
    print("날짜:", month, "월", date, "일")
    print("장소:", place)
    print("참석해 주시면 감사하겠습니다.")
    print("회신연락처 : aaa@bbb.com")

def party(month, date, place):
    print("파티에 초대합니다.")
    inputinfo(month, date, place)

def meeting(month, date, place):
    print("회의를 알려드립니다.")
    inputinfo(month, date, place)

def workshop(month, date, place):
    print("워크샵 공지드립니다.")
    inputinfo(month, date, place)
