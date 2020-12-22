#전역변수와 지역변수

command = "동쪽으로 가자"

def say():
    global command      # command 전역변
    command = "서쪽으로 가자"
    print(command)

print(command)
say()
print(command)
