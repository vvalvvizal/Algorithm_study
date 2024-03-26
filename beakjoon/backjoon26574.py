n = int(input())
lst = []
for _ in range(n):
    m = int(input())
    lst.append(m)

for i in lst:
    for _ in range(2):
        print(i , end=' ')
    print("")
