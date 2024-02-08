# # 시간초과

# # INF = float('inf')

# # def dijkstra(graph, start):
# #     n = len(graph)
# #     distance = [INF] * n
# #     visited = [False] * n

# #     distance[start] = 0

# #     for _ in range(n):
# #         min_dist = INF
# #         min_node = -1
# #         for j in range(n): #어디로 이동할지
# #             if not visited[j] and distance[j] < min_dist:
# #                 min_dist = distance[j]
# #                 min_node = j

# #         if min_node == -1:
# #             break

# #         visited[min_node] = True

# #         for v, w in graph[min_node]: #이동한 정점에서의 최단거리
# #             if not visited[v] and distance[min_node] + w < distance[v]:
# #                 distance[v] = distance[min_node] + w

# #     return distance

# # 입력 받기
# # V, E = map(int, input().split())
# # K = int(input())

# # 그래프 초기화
# # graph = [[] for _ in range(V + 1)]

# # 그래프 정보 입력 받기
# # for _ in range(E):
# #     u, v, w = map(int, input().split())
# #     graph[u].append((v, w))

# # 다익스트라 알고리즘 수행
# # shortest_paths = dijkstra(graph, K)

# # 출력
# # for i in range(1, V + 1):
# #     if shortest_paths[i] == INF:
# #         print("INF")
# #     else:
# #         print(shortest_paths[i])

##########################################################################
#우선순위큐 (heapq)
        


import heapq 
import sys
INF = float('inf')
def dijkstra(graph, start):
    n = len(graph)
    distance = [INF] * n
    visited = [False] * n

    distance[start] = 0
    pq = [(0, start)]  # 우선순위 큐

    while pq:
        dist, node = heapq.heappop(pq)

        # 이미 방문한 노드인 경우 무시
        if visited[node]:
            continue

        # 방문 표시
        visited[node] = True

        # 인접 노드 탐색
        for v, w in graph[node]:
            if not visited[v] and dist + w < distance[v]:
                distance[v] = dist + w
                heapq.heappush(pq, (distance[v], v))

    return distance



V, E = map(int, input().split())
K = int(input())

# 그래프 초기화
graph = [[] for _ in range(V + 1)]

# 그래프 정보 입력 받기
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

# 다익스트라 알고리즘 수행
shortest_paths = dijkstra(graph, K)

# 출력
for i in range(1, V + 1):
    if shortest_paths[i] == INF:
        print("INF")
    else:
        print(shortest_paths[i])