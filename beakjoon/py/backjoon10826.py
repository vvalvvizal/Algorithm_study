# import sys  
# sys.setrecursionlimit(10**5)

# def fibo(n):
#     if n == 0:
#         return 0
#     if n== 1:
#         return 1
#     return fibo(n-1)+fibo(n-2)


# m = int(input())
# print(fibo(m))
#재귀사용 시간초과 


#동적계획법. tabulation 

def fibo(n):
    fib = [0] * (n+2)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

m = int(input())
print(fibo(m))
