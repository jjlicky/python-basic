n=0
n2=0
answer = " "
file_count = []

while n<5:
    n=n+1
    count=n

    try:
        e=open("C:\\python1223\\vip"+str(count)+".txt")
        print(e.read())
        e.close()
    except FileNotFoundError:
        file_count.append(n)
        n2+=1

print(str(n2)+"개 파일이 없습니다.")


print("누락된 파일을 추가할까요?(yes/no)")
answer = input()

if answer == "yes":
    i=0
    while i < len(file_count):
        v=open("C:\\python1223\\vip"+str(file_count[i])+".txt",'w')
        print("vip"+str(file_count[i])+".txt 파일 생성함")
        v.close()
        i+=1
elif answer == "no":
    pass
