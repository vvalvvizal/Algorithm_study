n = int(input())
lst = {}

for _ in range(n):
    str = input()
    if str not in lst:
        lst[str] = 0
    else:
        lst[str]+=1
        
sorted_key = sorted(lst.keys())
#sorted(lst.items(), key= lambda x : x[1])
max_key = max(sorted_key, key=lst.get)
print(max_key)

