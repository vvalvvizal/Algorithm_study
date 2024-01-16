#그리디 44ms 
#그리디가 확실히  빠르긴하다 
n = int (input())
coin = [5,2]
count = 0
while n>0:
    if n%5 == 0:
        count += n//5
        n = n % 5 
    else:
        count += 1
        n-=2 

if n<0:
    print(-1)
else:
    print(count)


#동적계획법 76ms 

# def dp(n):
#     coin = [5,2] #내림차순 정렬 
#     dp = [float('inf')]*(n+1) #초기값을 무한대로 지정 
#     dp[0] = 0

#     for i in range(1,n+1):
#         for c in coin:
#             if i>=c and dp[i-c]+1<dp[i]:
#                 dp[i] = dp[i-c]+1
#     return dp[n] if dp[n] != float('inf') else -1


# n = int(input())
# print(dp(n))
