n = int(input())

skil = input()

count = 0
lr = 0
sk = 0
for i in skil:
    if i == 'L':
        lr +=1
    elif i == 'R':
        if lr >0:
            count+=1
            lr -=1
        else:
            break
    elif i == 'S':
        sk +=1
    elif i == 'K':
        if sk>0:
            count+=1
            sk -=1      
        else:
            break         
    else:#1~9
        count+=1

print(count)