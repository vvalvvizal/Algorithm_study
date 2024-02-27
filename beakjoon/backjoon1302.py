n = int(input())
lst = {}

for _ in range(n):
    str = input()
    if str not in lst:
        lst[str] = 0
    else:
        lst[str]+=1
        
sorted_key = sorted(lst.keys())

max_key = max(sorted_key, key=lst.get)
print(max_key)

