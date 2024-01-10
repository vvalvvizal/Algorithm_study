from collections import deque 
import sys

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    queue = deque([1])
    count = 0
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    while queue:
        v = queue.popleft()
        visited[v] = True
        for g in graph[v]:
            if not visited[g]:
                visited[g] = True
                queue.append(g)
                count+=1

    print(count)



