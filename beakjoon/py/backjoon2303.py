# n = int(input())
# lst = []
# for _ in range(n):
#     lst.append(list(map(int, input().split())))

# for idx, l in enumerate(lst):
#     max_num = -1
#     max_index = 0  # 최대값을 갖는 리스트의 인덱스를 저장할 변수
#     answer_index =0
#     answer_num = 0
#     for i in  range(n):
#         if max_num < current_sum:
#             max_num = current_sum
#             max_index = idx
#     if max_num >= answer_index:
#         answer_index = idx+1
#         answer_num = max_num

# print(answer_index)

from itertools import combinations

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
ans = 0
ans_max = 0
for i in range(n):
    comb = list(combinations(lst[i], 3))
    temp = 0
    for j in comb:
        temp = max(temp, sum(j) % 10)#일의자리수 중 max값 찾기 
    if temp >= ans_max:
        ans = i + 1
        ans_max = temp
print(ans)