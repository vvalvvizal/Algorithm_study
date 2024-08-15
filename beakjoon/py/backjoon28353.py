n , k = map(int,input().split())
lst = list(map(int, input().split()))
#3 4 5 6 7 9 
lst.sort()
start = 0
end = len(lst)-1 #5
count = 0
while start<end:
    if lst[start]+lst[end]>k:
        end-=1 
    elif lst[start]+lst[end]<=k:
        count+=1
        end-=1
        start+=1

print(count)