n = int(input())

for i in range(1,n+1):
    for j in range(i):
        print("*",end='')
        # print(" ",end='')
    # for k in range(n-i):
    #     # print("*",end='')
    #     print(" ",end='')
    print('')

for i in range(1,n):
    for k in range(n-i):
        print("*",end='')
    # for j in range(i):
    #     print(" ",end='')
    print('') 