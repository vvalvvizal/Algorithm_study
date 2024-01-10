n = int(input())
list_n= list(map(int, input().split()))
list_n.sort() #오름차순 정렬
m = int (input()) #찾아야하는 숫자카드 
list_m = list(map(int,input().split()))


result = []

for i in list_m:
    low = 0
    high = n-1
    while low<=high:
        mid = (high+low)//2
        if i < list_n[mid]:
            high = mid-1
        elif i>list_n[mid]:
            low = mid+1
        else:
            result.append(1)
            break
    else:
        result.append(0)
    
print(*result)