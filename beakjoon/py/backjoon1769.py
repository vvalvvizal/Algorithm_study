def trans(n):
    global count
    result = 0
    for nn in n:
        result += int(nn)
    return str(result)
    
    
n = input()
count = 0        
while int(n)>=10:
    count +=1
    n = trans(n)


print(count)
if int(n)%3==0:
    print('YES')
else:
    print('NO')