
from collections import Counter

n = input()

count = Counter(n)
result = []
odd = ''  # 홀수인 문자 따로 저장
oddnum = 0

keys_sorted = sorted(count.keys()) #딕셔너리 정렬해주기
for i in keys_sorted:
    for _ in range(count[i] // 2):
        result.append(i)

    if count[i] % 2 == 1:
        oddnum += 1
        odd = i  # 저장

if oddnum > 1:
    print("I'm Sorry Hansoo")
else:
    palindrome = result + [odd] + result[::-1]
    print(''.join(palindrome))
#딕셔너리 사용법 
#key : value 
#인덱스에 key를 넣으면 value가 나옴
    
#딕셔너리 정렬 
#sorted(dic.keys()) 
#values에 따라 정렬도 가능함!
            

#펠린드롬 조건 
#길이가 짝수이면 - 문자들이 짝수개 존재 
#길이가 홀수이면 - 홀수개인 문자가 하나, 나머지는 짝수개 존재 