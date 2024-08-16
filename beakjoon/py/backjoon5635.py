student = []
for _ in range(int(input())):
    n,d,m,y = input().strip().split()
    d,m,y = map(int,(d,m,y))
    student.append((y,m,d,n))#set
student.sort()
print(student[-1][3])
print(student[0][3])