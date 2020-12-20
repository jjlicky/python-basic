#문자열 내장 함수

s1 = "It's the miracle that the person who I like likes me."
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.capitalize())
print(s1.title())

s2 = 'Wonderful dreams'
print(s2.strip())
print(s2.lstrip())
print(s2.rstrip())
print(s2.replace("dreams", "days"))

s3 = "Dreams and goals"

print(s2.split())
print(s3.split("and"))

s4 = "Everything will be fine."

print(s4.count('a'))
print(len(s4))
print(s4.find('w'))
print(s4.find('k'))
