#세개의 정수를 입력받아 최대값 출력하는 프로그램

a, b, c = map(int, input().split())

if a>b :
    m=a
    if a>c:
        m=a
    else:
        m=c
else :
    m=b
    if b>c:
        m=b
    else:
        m=c
print(m)
