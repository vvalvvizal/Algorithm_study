a, b = map(int,input().split())
c = int(input())

b = c+b 
if b>=60:
    a = a + b//60
    b = b%60
if a>=24:
    a = a%24


print(f'{a} {b}')