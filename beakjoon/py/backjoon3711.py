# import sys


# t = int(input())
# for _ in range(t):

#     g = int(sys.stdin.readline())
#     lst = []
#     for _ in range(g):
#         tmp = int(sys.stdin.readline())
#         lst.append(tmp)
#     result = float('inf')
#     for m in range(1000000,0,-1):
#         flag = True
#         module = set()
#         for l in lst:
#             tmp = l%m
#             if tmp in module:
#                 flag = False
#             else:
#                 module.add(tmp)
#         if flag:
#             if m<result:
#                 result = m
#         else:
#             continue

#     print(result)


for _ in range(int(input())):
    n = int(input())
    numbers = [int(input()) for i in range(n)]
    result = 0

    while True:
        result += 1
        if len({i% result for i in numbers})==n:
            #{} 집합생성 
            print(result)
            break