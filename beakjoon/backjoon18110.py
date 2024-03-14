def roundd(n): #반올림 함수 
    if n - int(n)>=0.5:
        n = int(n)+1
    else:
        n = int(n)    
    return n



n = int(input())

if n==0:
    print(0)
else:
    lst = []
    for _ in range(n):
        tmp = int(input())
        lst.append(tmp)

    lst.sort() #오름차순 정렬 

    avg30 = n * 0.15
    cut = roundd(avg30)

    avg = 0
    count = 0
    for l in range(cut, n-cut):
        avg += lst[l]
        count +=1

    print(roundd(avg/count))
    



