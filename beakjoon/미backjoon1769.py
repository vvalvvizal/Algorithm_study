def trans(m):
    global count
    count+=1
    new_n = 0
    for s in str(m):
        new_n += int(s)
    return new_n
    
n = int(input())
count = 0
while n>9:
    n = trans(n)

print(count)
if n%3==0:
    print('YES')
else:
    print('NO')