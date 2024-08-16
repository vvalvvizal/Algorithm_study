t=0 #시나리오 번호 
while True:

    dict = set() #빼앗긴 리스트set
    t += 1 #시나리오 번호 증가 
    lst = []
    result = [] #돌려받은 학생 리스트 
    n = int(input()) #학생 수
    if n==0:
        break #종료조건 
    for _ in range(n):
        tmp = input()
        lst.append(tmp) #학생 이름 리스트에 추가 

    for _ in range(2*n-1):
        num, alphabet = input().split()
        if num not in dict:
            dict.add(num)
        else: #이미 거친 학생번호이면 
            result.append(int(num))
    # print(f"result : {result}")
    for l in range(len(lst)):
        if (l+1) not in result:
            print(f"{t} {lst[l]}")
