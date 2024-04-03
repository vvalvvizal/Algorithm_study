import sys


t = int(input())
for _ in range(t):

    g = int(sys.stdin.readline())
    lst = []
    for _ in range(g):
        tmp = int(sys.stdin.readline())
        lst.append(tmp)
    result = float('inf')
    for m in range(1000000,0,-1):
        flag = True
        module = set()
        for l in lst:
            tmp = l%m
            if tmp in module:
                flag = False
            else:
                module.add(tmp)
        if flag:
            if m<result:
                result = m
        else:
            continue

    print(result)

