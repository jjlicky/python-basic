where='경기도'
days='1박2일'

def reservation():
    global where
    global days

    where=input()

    if where == '경기도':
        days = '당일여행'
    else:
        days = '2박3일'
        
print(where+'로'+days+'여행갈까?')
print("여행예약시스템 : 여행지 입력하세요")
reservation()
print(where+" 여행일정 추천: "+days)
