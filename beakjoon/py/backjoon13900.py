n = int(input())

numlist = list(map(int, input().split()))

'''
2 3 2 4


결합법칙
1) 2 * 3 + 2 * 2 + 2* 4 = 6 + 4 + 8 = 18
2 ) 2 * (3+2+4) = 18

'''
sum_num= sum(numlist) #list안의 아이템의 합 
result =0 

for i in numlist:
    sum_num = sum_num - i
    result += i * sum_num

print(result)