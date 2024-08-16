# n, m, b = map(int,input().split())
# land = [[]*m for _ in range(n)]

# for i in range(n):
#     land[i] = list(map(int,input().split()))#땅 저장 

# avg = 0
# for l in land:
#     for p in l:
#         avg += p

# avg/=(n*m)
# avg = round(avg)

# diff = float('inf')
# target = 0
# count = 0
# for l in land:
#     for p in l:
#         if diff>abs(avg-p):
#             diff = abs(avg-p) #편차가 가장 적은 땅 찾기 
#             target = p
#         else:
#             continue

# print(target)
# for l in land:
#     for p in l:
#         if p != target:
#             if p>target:
#                 count += (abs(p-target)*2)
#             else:
#                 count+=(abs(p-target)*1)

# print(f"{count} {target}")

import sys

n, m, b = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = float('inf')
idx = 0
for target in range(257): #브루트포스 작은값->큰값이기때문에 높은 층으로 갱신됨 
    max_target, min_target = 0, 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] >= target:
                max_target += graph[i][j] - target #오버된거 
            else: #작으면 
                min_target += target - graph[i][j] #부족한거 

        
    if max_target + b >= min_target: #오버돼서 인벤토리 들어온거 + 기존 인벤토리블록 >= 빼야하는 블록
        if min_target + (max_target * 2) <= answer: #빼는데 걸리는 시간 
            answer = min_target + (max_target * 2) # 최저 시간 갱신
            idx = target # 층수

print(answer, idx)