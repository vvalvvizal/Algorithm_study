n , m = map(int, input().split())
num_list = list(map(int, input().split()))

count = 0
left = 0
sum = 0

for right in range(n):
    sum += num_list[right]
    if sum == m:
            count +=1
    while sum>m:
        sum -= num_list[left]
        if sum == m:
            count +=1
        left +=1
        
print(count)


