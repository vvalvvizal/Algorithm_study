# n = int(input())

# lst = {}  # 빈 딕셔너리 생성
# for _ in range(n):
#     age, name = input().split()
#     lst[name] = int(age)  # 나이를 정수형으로 변환하여 저장

# # 딕셔너리를 값에 따라 정렬
# sortedlst = dict(sorted(lst.items(), key=lambda item: item[1]))
# #sorted 함수의 key 매개변수는 정렬기준을 지정 
# #lambda함수는 한 줄로 간단한 함수 작성 
# #item을 받아서 item[1](표현식)을 반환함 
# # 정렬된 딕셔너리를 출력
# for name, age in sortedlst.items():
#     print(f'{age} {name}')

n = int(input())
member_lst = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member_lst.append((age, name))

member_lst.sort(key = lambda x : x[0])	## (age, name)에서 age만 비교

for i in member_lst:
    print(i[0], i[1])