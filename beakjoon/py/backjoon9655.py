n = int(input())
if n % 2 == 0:
    print('CY')
else:
    print('SK')


# import sys
# input = sys.stdin.readline

# N = int(input())
# dp = [-1] * 1001

#SK
# dp[1] = 1

#CY
# dp[2] = 0

#SK
# dp[3] = 1

# for i in range(4, N + 1):
#     if dp[i-1] or dp[i-3]:
#         dp[i] = 0
#     else:
#         dp[i] = 1

# if dp[N] == 0:
#   print("CY")
# else:
#   print("SK")  