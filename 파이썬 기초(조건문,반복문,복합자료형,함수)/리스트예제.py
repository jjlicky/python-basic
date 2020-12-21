lst=[1,2,3,4,5,4,3,2,1]
value=3
while True:
    lst.remove(value)
    if value not in lst:
        break
print(lst)
