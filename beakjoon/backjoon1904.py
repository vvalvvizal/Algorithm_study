#동적계획법으로 풀려면
def find_answer(n):
    dp = [0]*(n+1)
    
    if n>=1:
        dp[1] = 1 #타일 하나로 만들 수 있는 가짓수
    if n>=2:
        dp[2] = 2 #타일 두개로 만들 수 있는 가짓수 
    
    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2])%15746 #오버플로우 방지 
        #dp[3] = dp[2] + dp[1]
        #dp[4] = dp[3] + dp[2] = dp[2] + dp[1] + dp[1] 

        #dp[1] = 1  #1개 
        #dp[2] = 00,11 #2개 
        #dp[3] = 001, 100,111 #3개  

        #dp[4] = 0011, 1001, 1111, 1100, 0000 #5개  

        #dp[5] = 00111, 00001, 10011, 11001, 11111, 10000, 11100, 00100 #8개 
    return dp[n]

n = int(input())
result = find_answer(n)
print(result)