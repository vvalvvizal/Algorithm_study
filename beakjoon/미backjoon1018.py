n, m = map(int, input().split())
lst = [list(input()) for _ in range(m)]

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]  # 상 하 좌 우
count = 0

for r in range(m):
    for c in range(n):
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < m and 0 <= nc < n: 
                if lst[nr][nc] == lst[r][c]:
                    if lst[r][c] == 'W': 
                        lst[r][c] = 'B'
                    elif lst[r][c] == 'B':
                        lst[r][c] = 'W'
                    count += 1

print(count)
