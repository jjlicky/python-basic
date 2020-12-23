n=0
n2=0

while n<5:
    n=n+1
    count=n

    try:
        e=open("C:\\python1223\\vip"+str(count)+".txt")
        print(e.read())
        e.close()
    except FileNotFoundError:
        n2+=1

print(str(n2)+"개 파일이 없습니다.")
