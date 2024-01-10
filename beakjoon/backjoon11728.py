# n, m = map(int, input().split())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# a = 0
# b = 0
# result = []

# while True:
#     if A[a]<=B[b]:
#         result.append(A[a])
#         a+=1
#     else : 
#         result.append(B[b])
#         b += 1
#     if a == n or b == m :
#         result += A[a:] + B[b:]
#         break

# print(*result)

n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = A +B
C.sort()

answer = ' '.join(map(str,C))
print(answer)