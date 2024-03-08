n, m, b = map(int,input().split())
land = [[]*m for _ in range(n)]

for i in range(n):
    land[i] = list(map(int,input().split()))#땅 저장 

dict = {}

lst = [-1]
for l in land:
    for pos in l:
        if lst:
            tmp = lst.pop()
            if tmp != pos:
                dict[pos]=1
            else:
                dict[pos]+=1
        lst.append(pos)

maxnum = max(dict, key=dict.get)

for l in land:
    for pos in l:
        if pos != maxnum:
            