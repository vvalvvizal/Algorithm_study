
#동적계획법으로 풀려면
def find_answer(n):
    dp = [0]*(n+1)

    dp[1] = 1
    dp[2] = 2 

    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2])%15746 #오버플로우 방지 

    return dp[n]

n = int(input())

result = find_answer(n)
print(result)