def x(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()
x(3, "안녕하세요.","오늘도","즐거운 하루 보내세요.")
