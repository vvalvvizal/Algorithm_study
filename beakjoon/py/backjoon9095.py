#동적계획법

def find_answer(n):
    dp = [0]*(n+1)
    #1,2,3의 합으로 나타내는 방법
    if n>=1:
        dp[1] = 1 #1 
    if n>=2:
        dp[2] = 2 #1+1, 2 
    if n>=3:
        dp[3] = 4
    #dp[4] = 7

    for i in range(4,n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(find_answer(n))

