# n, m = map(int, input().split())
# lst = [list(input()) for _ in range(m)]
# result = 0
# dr = [1, -1, 0, 0]
# dc = [0, 0, -1, 1]  # 상 하 좌 우
# for r in range(m):
#     for c in range(n):
#         count = 0
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < m and 0 <= nc < n: 
#                 if lst[nr][nc] == lst[r][c]:
#                     count+=1
#                     if count==4:
#                         result+=1
#                         if lst[r][c] == 'W':
#                             lst[r][c] = 'B'
#                             break
#                         elif lst[r][c] == 'B':
#                             lst[r][c] = 'W'
#                             break         
        
# print(result)


N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7): #8x8칸 만들기 시작하는 위치 
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:#8방향 이동한 i+j가 짝수라면 기존 색[a][b]과 동일 
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))