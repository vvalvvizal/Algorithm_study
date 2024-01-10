
# def find(nx, ny,graph):
#     dx = [1,-1,0,0]
#     dy =[0, 0, -1, 1]
#     global count, result
#     graph[nx][ny] = 0 #방문한 정점은 0으로 변경 
#     if nx==m and ny == n:
#         result = count

#     for y in dy:
#         for x in dx:
#             if nx+x<1 and nx+x>m and ny+y<1 and ny+y>n:
#                 continue
#             if graph[ny+y][nx+x]==1:
#                 count+=1
#                 find(ny+y,nx+x,graph)

# count = 0
# result = 0
# n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for i in range(1,n+1):
#     graph[i].append(0)
#     tmp = input()
#     for j in tmp:
#         graph[i].append(j)

# find(1,1,graph)

# print(result)
# # print(graph)
# #     [[],
# #       [0, '1', '0', '1', '1', '1', '1'], 
# #       [0, '1', '0', '1', '0', '1', '0'], 
# #       [0, '1', '0', '1', '0', '1', '1'],
# #       [0, '1', '1', '1', '0', '1', '1']] 어디서 인덱스 에러가 나는거야


from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def bfs(start_x, start_y):

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(start_x, start_y)])

    while queue:
        x, y = queue.popleft()

        # if x == m and y == n:
        #     return graph[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]


            if nx < 0 or nx >= n or ny<0 or ny>=m :
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n-1][m-1]


print(bfs(0,0))