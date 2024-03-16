t=0

while True:
    t += 1 #시나리오 번호 
    lst = []
    check = [0] * (n+1)
    n = int(input())
    if n==0:
        break 
    for _ in range(n):
        tmp = input()
        lst.append(tmp)
    
    num, a = input().split()
    check[int(num)]

