'''n, m = map(int, input().strip().split())

num_list = list(map(int, input().strip().split()))


for i in range(m):
    sum=0
    s, e = map(int, input().strip().split())
    s = s-1
    e = e-1
    while(s<=e):
        sum += num_list[s]
        s+=1
    print(sum)


'''
        












import sys

n, m = map (int, sys.stdin.readline().strip().split())


list = list(map(int, sys.stdin.readline().strip().split()))

sumlist = [0]
total = 0

for i in list:
    total += i
    sumlist.append(total) 
    print(sumlist)
    #누적합 리스트에 추가
    # 0 5 9 12 14 15 
    # 1 2 -> 9 
    # 1 3 -> 12

for i in range(m):
    s,e = map (int, sys.stdin.readline().strip().split())
    print(sumlist[e]-sumlist[s-1])



