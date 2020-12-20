#format 함수

print("I have {} apples.".format(5))
print("I have {0} apples.".format("five"))
print("I have {0} apples. I eat them {1}".format(5, "everyday"))

a=3 
print("I have {} apples.".format(a))

print("I have {a} apples. I ate {b}".format(a=3, b=2))

print("{} {}".format(1,2,3))

a="{:10d}".format(35)
print(a)
b="{:010d}".format(35)
print(b)
c="{:10.2f}".format(35.21789)
print(c)

fruit = 'mango'
cnt = 5
print(f'I have {cnt} {fruit}.')
