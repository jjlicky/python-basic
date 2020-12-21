def eight(n):
    count=0
    for i in range(n):
        for j in str(i):
            if j=='8':
            
                count+=1
                print(str(i), end=" ")
    print()
    print("8의 개수는 %d입니다."%count)
eight(30)
