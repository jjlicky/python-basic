a=[]
b=[]
value=0
for i in range(0,100):
    i+=1
    a.append(value)
    value+=2
for i in range(0,100):
    b=a
    b.reverse()
    break
print("b[0]은 %d, b[99]는 %d" %(b[0], b[99]))
