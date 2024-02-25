# def is_sejunnum(n_, k):
#     max_n = -1
#     lst=[1]
#     for j in range(2, n_ + 1):
#         while n_ % j == 0:
#             if j not in lst:
#                 lst.append(j)
#             n_ //= j
#     max_n = max(max_n, lst.pop())
#     if max_n <= k:
#         return True
#     else:
#         return False

# n = int(input())
# k = int(input())
# count = 0
# for i in range(1, n + 1):
#     if is_sejunnum(i, k):
#         count += 1 
# print(count)
#시간초과




# 입력 받기
n = int(input())
k = int(input())

# 에라토스 테네스의 체
primeList = [True] * (n+1)  # 최대 1부터 N까지 소수 판별
for i in range(2, int(n**0.5)+1): #제곱근 
    if primeList[i]:  # i가 소수라면
        for j in range(2 * i, n+1, i):  #i의 배수들은 False
            primeList[j] = False

k_number = [1]*(n+1)
for i in range(2, n+1):
    if primeList[i] and i > k:
        for j in range(i, n+1, i):
            k_number[j] = 0
print(sum(k_number)-1)