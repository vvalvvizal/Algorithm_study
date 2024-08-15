n, m = map(int, input().split())

s = []
count = 0
for _ in range(n):
    s.append(input())
for i in range(m):
    str = input()
    if str in s:
        count+=1

print(count)