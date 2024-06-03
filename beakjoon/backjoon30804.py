n = int(input())
tanghuru = list(map(int, input().split()))
left=0
fruit_list = {} #딕셔너리 생성 
maxlength = 0

for right in range(n):
    if tanghuru[right] in fruit_list:
        fruit_list[tanghuru[right]]+=1
    else:
        fruit_list[tanghuru[right]]=1

    while len(fruit_list)>2:
        fruit_list[tanghuru[left]]-=1
        if fruit_list[tanghuru[left]]==0:
            del fruit_list[tanghuru[left]]
        left+=1
    #right는 n-1 = 4  
    #left는 1
    maxlength = max(maxlength,(right-left)+1)

print(maxlength)