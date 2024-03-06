n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

result = []  # 최대값과 해당 인덱스를 저장할 리스트

for idx, l in enumerate(lst):
    max_num = -1
    max_index = 0  # 최대값을 갖는 리스트의 인덱스를 저장할 변수
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                # 현재 조합의 합 계산
                current_sum = sum((l[i], l[j], l[k])) % 10
                # 최대값 갱신
                if max_num < current_sum:
                    max_num = current_sum
                    max_index = idx

    result.append((max_num, max_index))

# result 중복되는 최댓값들의 인덱스 중 가장 큰 값의 인덱스 반환
max_index = max(result, key=lambda x: x[0])[1]
print(max_index+1)
