
#팩토리얼?
#0! = 0 
#1! = 1
#2! = 2 
#3! = 6 
#4! = 4321 = 24 
#..... n! = (n-1)! * n 
#10! = 10 9 8 7 6 5 4 3 2 1 = 3628800 

#2와 5의 개수 
#10이 얼마나 존재하나 -> 뒤의 0개수 
n = int(input())

a=0
b=0
c=0
for i in range(2,n+1):
    num = i
    while num%2==0:
        num/=2
        a +=1 
    while num%5==0:
        num/=5
        b+=1

result = min(a,b)
print(result)