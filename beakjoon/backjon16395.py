# #dp 
# memorization (하향식). 재귀 - 시간초과
# def memorization(n, k):
#     if n==1 or k==1:
#         return 1
#     if n == k:
#         return 1 
#     return memorization(n-1,k-1)+memorization(n-1,k)

# n, k = map(int, input().split())
# dp = [[0]*(n+1) for _ in range(n+1)]

# dp[n][k] = memorization(n,k) #3,2 

# print(dp[n][k])

#tabulation(상향식)
def tabulation(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(k + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][k]

n, k = map(int, input().split())
result = tabulation(n - 1, k - 1)
print(result)
