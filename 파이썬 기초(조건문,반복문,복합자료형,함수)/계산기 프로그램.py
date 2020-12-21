def calculator(cal,n,m):
    if cal=='+':
        return n+m
    elif cal=='-':
        return n-m
    elif cal=='*':
        return n*m
    else :
        return n/m
cal=input("어떤 연산을 수행할까요? : ")
n,m=map(int,input("두 수를 입력하세요 :").split())
print("%d %s %d = %d"%(n,cal,m,calculator(cal,n,m)))
