from collections import deque

n = int(input())
lst = list(map(int,input().split()))

type = 0 

slow = 0
maxi = 0
q = deque(lst)
while q:
    for fast in range(1, len(q)):
        if q[slow] != q[fast]:
            slow +=1
            q[slow] = q[fast]
    print(q)
    if slow+1>maxi:
        maxi = slow+1
    for i in range(n+1):#브루트포스  
        q = deque(lst)
        tmp = q.pop()
        for j in range(n+1):
            if q:
                tmp = q.popleft()

    print(maxi)