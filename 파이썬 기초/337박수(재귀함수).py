def cheering337(n):
    if n < 14:
        print("짝")

        if(n%3==0 and n<7):
            print(" ")
        n+=1
        cheering337(n)

cheering337(1)
