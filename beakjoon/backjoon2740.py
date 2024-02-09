N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

C = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for m in range(M):
         C[i][j]+=A[i][m]*B[m][j]


for row in C:
    print(' '.join(map(str,row)))
