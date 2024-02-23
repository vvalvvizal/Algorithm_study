n = int(input())
visited = list(map(int, input().split()))
count = 0
result = [[]for _ in range(n)]

while True:
    if all(x==-1 for x in visited):
        #visited의 모든 요소가 -1이면 
        break
    for i in range(n):
        if visited[i]>0:
            visited[i]-=1
            count+=1
        else:
            continue
        for j in range(n):
            if visited[j]==0:
                result[j]=count
                visited[j]=-1
       
    
print(*result)

