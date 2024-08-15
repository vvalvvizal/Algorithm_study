#투포인터 

n = int(input())

lst = list(map(int, input().split()))
x = int(input())

count = 0
p1 = 0
p2 =len(lst)-1

lst.sort()
while p1<p2:
    if lst[p1]+lst[p2] > x:
      p2-=1 
    elif lst[p1] + lst[p2] < x:
       p1+=1 
    elif lst[p1] + lst[p2] == x:
       count += 1
       p2-=1
       p1+=1

print(count)