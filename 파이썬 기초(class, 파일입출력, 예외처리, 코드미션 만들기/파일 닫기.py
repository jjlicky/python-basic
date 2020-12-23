print("1.파일을 엽니다.")
m1 = open("C:\\python1223\\메모.txt",'r')

print("2.파일을 읽습니다.")
read_m1 = m1.read()

print("3.읽은 내용을 출력합니다.")
print("__출력내용 아래__")
print(read_m1)

print("4.파일을 닫습니다.")
m1.close()
print("5.파일을 닫았습니다.")
