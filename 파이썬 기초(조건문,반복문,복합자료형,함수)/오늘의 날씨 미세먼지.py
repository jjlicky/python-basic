def weather(w):
    if w == 'cloudy':
        print("오늘의 날씨는 <흐림>입니다.")
    if w == 'sunny':
        print("오늘의 날씨는 <맑음>입니다.")
    if w == 'rainy':
        print("오늘의 날씨는 <비>입니다.")
    dust=[0]
    for i in range(1,101):
        dust.extend([i])
    if (air in dust[:16]):
        print("오늘의 미세먼지는 <좋음>입니다.")
    elif (air in dust[16:36]):
        print("오늘의 미세먼지는 <보통>입니다.")
    elif (air in dust[37:76]):
        print("오늘의 미세먼지는 <나쁨>입니다.")
    elif (air in dust[75:]):
        print("오늘의 미세먼지는 <매우나쁨>입니다.")
w= 'cloudy'
air = 80
weather(w)
