def eight(n):
    count = 0
    for x in range(1,n+1):
        if('8' in str(x)):
            count+=1
            print(str(x), end=" ")
    print()
    print("8의 개수는 %d개입니다."%count)
    
eight(30)
