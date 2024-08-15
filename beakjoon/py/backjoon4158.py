import sys

while True:
    m, n =map(int,input().split())

    if m==0 and n==0:
        break


    sangun = []
    sunyeong = []
    for _ in range(n):
        tmp = int(sys.stdin.readline())
        sangun.append(tmp)#오름차순

    for _ in range(m):
        tmp = int(sys.stdin.readline())
        sunyeong.append(tmp)#오름차순 

    count = 0

    for s in sangun:
        low = 0
        high = len(sunyeong)-1
        while low<=high:
            mid = (low+high)//2
            if s < sunyeong[mid]:
                high = mid-1
            elif s > sunyeong[mid]:
                low = mid+1
            else:
                count+=1
                break

    print(count)