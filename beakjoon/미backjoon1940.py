n = int(input())
m = int(input())
material = list(map(int, input().split()))

materialcount = 0
left = 0
sum = 0
count = 0
for right in range(n):
    sum += material[right]
    materialcount+=1 #사용한 재료의 수 
    if sum == m and materialcount==2: #m이 되었을때, 재료수가 2개일때
        count +=1 
        materialcount=0 #사용 재료수 0으로 리셋
        sum=0
    while sum>=m and materialcount<2: #만들어야하는 수가 합계보다 작을때, 사용 재료가 2보다 작을 때 
        sum -= material[left] #앞에것부터 합계에서 빼기 
        materialcount-=1#사용 재료 수 줄이기 
        if sum == m:#합계가 정확히 m이되면 
            count +=1
            materialcount=0
            sum=0
    left += 1
    

    
print(count)