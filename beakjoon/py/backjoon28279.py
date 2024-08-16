from collections import deque
import sys

q = deque()
n = int(input())
for _ in range(n):
    order = sys.stdin.readline().split()

    if order[0] == '1': 
        q.appendleft(order[1])
    elif order[0]=='2':
        q.append(order[1])
    elif order[0]=='3':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif order[0]=='4':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif order[0]=='5':
        print(len(q))
    elif order[0]=='6':
        if q:
            print(0)
        else:
            print(1)
    elif order[0]=='7':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)