from collections import deque 

# 입력 받기
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 방향 설정: 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue = deque([])

# 초기 익은 토마토 위치 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

# BFS 수행
while queue:
    r, c = queue.popleft()

    # 네 방향으로 탐색
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        # 범위 안에 있고, 익지 않은 토마토인 경우
        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and graph[nr][nc] == 0:
            queue.append((nr, nc))
            visited[nr][nc] = True
            graph[nr][nc] = graph[r][c] + 1

# 최대 일수 찾기
max_day = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
        max_day = max(max_day, graph[i][j])

print(max_day - 1)  # 첫 토마토가 1일부터 익기 시작했으므로, 1을 빼줌
