#동적계획법
#tabulation 상향식 
#반복문을 이용하여 작은 것에서 큰것 계산 

def dp(n):
    tab = [0] * (n+1)
    if n>=1:
        tab[1] = 4
    if n>=2:
        tab[2] = 6 
    for i in range(3,n+1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[n]

       

n = int(input())
print(dp(n))

