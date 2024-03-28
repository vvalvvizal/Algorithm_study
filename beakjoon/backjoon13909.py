# n = int(input())

# window = [0] * n

# for person in range(1, n + 1):  # 사람
#     for i in range(person - 1, n, person):  # 창문
#         # 해당 창문의 상태를 변경합니다.
#         window[i] ^= 1 #비트연산자

# count = 0

# for state in window:
#     count += state

# print(count)
#메모리 초과 


#닫힘 - 약수 1개 (열림) - 약수 2개 (닫힘) - 약수 3개 (열림)
#약수의 개수가 홀수 -> 창문 열림 

#약수가 홀수인 것, 제곱수 
# 9 : 1 3 9 
# 8 : 1 2 4 8 

#10 : 1 2 

n = int(input())
count = 0
for i in range(1, n+1):
    if i**2 <= n: 
        count +=1
    else:
        break
print(count)