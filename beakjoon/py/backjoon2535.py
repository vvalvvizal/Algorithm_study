n = int(input())

lst = [[] for _ in range(n+1)]
check = [0]*(n+1)
cut = []
for i in range(1,n+1):
    contry, student, score = map(int,input().split())
    lst[i].append(contry)
    lst[i].append(student)
    lst[i].append(score)
    
count = 3
sorted_lst = sorted(lst[1:], key=lambda x : x[2], reverse=True)
for l in sorted_lst:
    con = l[0]
    std = l[1]
    if con not in cut:
        if check[con]<2:
            check[con]+=1
            if count>0:
                print(f"{con} {std}")
                count-=1
            else:
                break
        else:
            cut.append(con)
    
    