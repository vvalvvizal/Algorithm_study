def stack(v, graph, visited):
    global count 
    # print(v)
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            stack(i, graph, visited)
            count += 1



count = 0
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
    
stack(1 ,graph, visited)


print(count)

