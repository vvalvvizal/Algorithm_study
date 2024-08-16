for _ in range(int(input())):
    n, x, y = map(int, input().split()) #참가자 수 , 트랙 길이, 부스터 한계치 
    v = list(map(int,input().split())) #속도 
    
    winner = max(v)

    if v.count(winner)==1 and v[n-1]==winner:
        print(0)
        continue
    else:
        winner = x/winner #초로 바꿈 

        l = 0
        h = y
        while l<=h:
            m = (l+h)//2
            boost = ((x-m)/v[-1])+1

            if boost >= winner:
                l = m +1
            else:
                h = m-1

        if l>y:
            print(-1)
        else:
            print(l)

