#동적계획법

def solved_problem(n, dp):
    dp[0] = 1 

    for i in range(1, n+1):#1~n
        for j in range(i): #0~i-1
            dp[i] += dp[j]*dp[i-j-1]
    return dp[n]

n = int(input())
dp = [0] * (n+1)
print(solved_problem(n, dp))
