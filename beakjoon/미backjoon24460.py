from collections import deque
import heapq #최소힙 

def devide_conquer(n): 
    q1 = []
    q2 = []
    q3 =[]
    q4 = []
    result = []
    for i in range(n//2):
        for j in range(n//2):
            heapq.heappush(q1,holl[i][j])

    for i in range(n//2,n):
        for j in range(n//2, n):
            heapq.heappush(q4,holl[i][j])
    for i in range(n//2):
        for j in range(n//2,n):
            heapq.heappush(q2,holl[i][j])
    for i in range(n//2, n):
        for j in range(n//2):
            heapq.heappush(q3,holl[i][j])
    heapq.heappop(q1)
    heapq.heappop(q2)
    heapq.heappop(q3)
    heapq.heappop(q4)


    heapq.heappush(result, heapq.heappop(q1))
    heapq.heappush(result, heapq.heappop(q2))
    heapq.heappush(result, heapq.heappop(q3))
    heapq.heappush(result, heapq.heappop(q4))
    
    print(heapq.heappop(result))

    if n==1:
        return heapq.heappop(result)
    else:
        return devide_conquer(n//2)


n = int (input())
holl = [[]*n for _ in range(n)]
for i in range(n):
    holl[i] = list(map(int,input().split()))

min = devide_conquer(n)
print(min)