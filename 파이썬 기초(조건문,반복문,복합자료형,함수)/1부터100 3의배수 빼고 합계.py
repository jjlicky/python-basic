sum=0
for i in range(1,101):
    i+=1
    if i%3 ==0:
        continue
    sum+=i
print("합계는",sum)
