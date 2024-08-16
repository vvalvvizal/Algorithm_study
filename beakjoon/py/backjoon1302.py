n = int(input())
lst = {}

for _ in range(n):
    str = input()
    if str not in lst:
        lst[str] = 0
    else:
        lst[str]+=1
        
sorted_key = sorted(lst.keys()) #키들만 정렬해서 반환 

max_key = max(sorted_key, key= lambda x: lst[x]) #40ms 
#max_key = max(sorted_key, key=lst.get) #44ms
#get()은 key에 대한 value를 반환해주는 함수
print(max_key)

