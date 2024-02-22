def is_sejunnum(n_, k):
    max_n = -1
    lst=[1]
    for j in range(2, n_ + 1):
        while n_ % j == 0:
            if j not in lst:
                lst.append(j)
            n_ //= j
    max_n = max(max_n, lst.pop())
    if max_n <= k:
        return True
    else:
        return False

n = int(input())
k = int(input())
count = 0
for i in range(1, n + 1):
    if is_sejunnum(i, k):
        count += 1 
print(count)
