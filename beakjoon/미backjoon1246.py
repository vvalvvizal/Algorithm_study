n, m = map(int, input().split())
lst = []
for _ in range(m):
    lst.append(int(input()))

lst.sort() # 오름차순 정렬

maxnum = -1
maxi = 0
# 그리디
for i in range(m):
    egg = min(m-i,n) #달걀 개수 n, m명인데 m<i개 사는 경우 n(달걀최대개수)으로 바꿔줌

    if res < lst[i] * egg:
        