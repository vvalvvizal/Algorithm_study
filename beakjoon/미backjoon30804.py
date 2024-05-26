from collections import deque

n = int(input())
lst = list(map(int,input().split()))

# 투포인터 l,r 과 빠른, 느린 
s = 0
f = 0
q = deque(lst)
