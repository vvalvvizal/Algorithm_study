

def dp_tab(n, lst):
    count = 0
    tab = [1] * (n + 1)
    tab2 = [1] * (n+1)
    for i in range(1, n):  # 증가수열
        if lst[i - 1] <= lst[i]:
            tab[i] = tab[i - 1] + 1      


    for i in range(n-1, 0, -1):  # 감소수열
        if lst[i] <= lst[i - 1]:
            tab2[i-1] = tab2[i] + 1 

    max1 = max(tab)
    max2 = max(tab2)

    return max(max1,max2)

n = int(input())
lst = list(map(int, input().split()))

# tabulation
# bottom-up
print(dp_tab(n, lst))
