import sys
from collections import deque

def dfs(now, graph, visited):
    visited[now] = True
    print(now, end=' ')
    for i in graph[now]:
        if not visited[i]:
            dfs(i, graph, visited)

def bfs(start, graph, visited): #시작정점 v 
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end =' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True 


        


n, m, v = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1,n+1):
    graph[i].sort()
    

dfs(v, graph, visited)
print()
bfs(v, graph, visited)



