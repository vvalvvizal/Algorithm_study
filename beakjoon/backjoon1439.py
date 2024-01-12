change = []
a = input()
isOdd = False 
for i in range(1,len(a)):
    if a[i-1] != a[i]: #바로 앞의 숫자와 동일하지 않으면 
        change.append(i) #바껴야할 연속된 지점 체크 
    

if len(change)%2==1:#홀수이면 
    isOdd = True
result = len(change)//2

if isOdd:
    result+=1

print(result)

