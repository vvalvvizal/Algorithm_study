def dfs(v, count):
    global result
    visited[v] = True

    if v == b:
        result = count
        return

    for i in graph[v]:
        if not visited[i]:
            #방문하지 않았다면
            dfs(i, count+1)

count = 0
result = -1
n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x,y = map(int, input().split())
    # x는 y의 부모번호 7
    graph[x].append(y)
    graph[y].append(x)

dfs(a, 0)
print(result)

