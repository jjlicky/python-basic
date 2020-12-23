todo1 = open("C:\\python1223\\todo.txt",'r')

print(todo1.read())

todo1 = open("C:\\python1223\\todo.txt",'w')

todo1.write("\n1.파이썬 강의 복습")
todo1.write("\n2.c언어 강의듣고 복습")
todo1.write("\n3.전담 문제점 찾고 flexing")

todo1.close()
