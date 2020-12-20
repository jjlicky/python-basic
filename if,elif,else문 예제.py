#if,else,elif문 예제
#사과, 오렌지 다있으면 "good!", 하나만있으면 "not bad!", 없으면 "Oh my god!"

apple = 23
orange = 0
if (apple and orange)!=0:
    print("good!")
elif (apple or orange)!=0:
    print("not bad!")
else:
    print("Oh my god!")
    
