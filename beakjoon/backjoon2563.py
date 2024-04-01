#세로 가로 각각 10 
n = int(input())

array = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int,input().split())

    for i in range(y,y+10):
        idx_y = i 
        for j in range(x,x+10):
            idx_x = j
            if array[idx_y][idx_x]==0:
                array[idx_y][idx_x]=1
            else:
                continue

sumarray = 0
for i in range(100):
    sumarray += sum(array[i])

print(sumarray)