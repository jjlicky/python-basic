import sys

f=open("출력결과.txt",'w')
stdout=sys.stdout
sys.stdout=f

print("메모장에")
print("출력결과를")
print("저장하는법")

f.close()
sys.stdout=stdout
