# n, m = map(int, input().split())
# lst = []
# for _ in range(m):
#     lst.append(int(input()))

# lst.sort()
# # 2 7 8 10
# maxnum = -1
# maxi = 0

#구매하는 달걀개수 (m)이 n보다 큰 경우 체크해야했음. 

# for i in range(max(lst), 1 ,-1): # 모든 숫자 확인할 필요 없었음. 
#     count = 0
#     for l in lst: #필요없는 이중포문 
#         if l>=i:
#             count+=1
#     result = i*count

#     if result >= maxnum:
#         maxnum = result
#         maxi = i

# print(f'{maxi} {maxnum}')


n, m = map(int, input().split())
lst = []
for _ in range(m):
    lst.append(int(input()))

lst.sort() # 오름차순 정렬

res = 0
target = 0
# 그리디
for i in range(m):
    #i의 범위는 0~m-1
    
    #몇 명의 고객이 사갔나 = i
    egg = min(m-i,n)
    #m-i : 현재고객부터 마지막고객

    if res < lst[i] * egg:
        res = lst[i] * egg  #수익 초기화  
        target = lst[i] #달걀 가격 초기화 
        
print(target, res)