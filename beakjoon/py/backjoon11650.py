n = int(input())

lst = []

for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))

lst.sort(key=lambda x: (x[0], x[1]))

for pair in lst:
    print(f'{pair[0]} {pair[1]}')
