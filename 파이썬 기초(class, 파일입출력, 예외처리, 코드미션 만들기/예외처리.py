

try:
    print("1.파일 invitation1을 엽니다.")
    v=open("C:\\python1223\\invitation1.txt",'r')
    print(v.read())

    print("2.파일 invitation2을 엽니다.")
    v=open("C:\\python1223\\invitation2.txt",'r')
    print(v2.read())
except FileNotFoundError:
    print("해당 파일이 없습니다.")
