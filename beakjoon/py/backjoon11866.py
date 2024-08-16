from collections import deque 

queue = deque()
lst =[]

n, k = map(int, input().split())
for i in range(1,n+1):
    queue.append(i)


for _ in range(n):
    queue.rotate(-k)
    # print(queue)
    lst.append(queue.pop())

print('<', end='')
for j in lst:
    if lst.index(j)>=n-1:
        print(j,end='>')
    else:
        print(j,end=', ')


