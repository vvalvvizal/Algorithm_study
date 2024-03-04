def devide_conquer(n, holl):

    # 분할 정복
    divided_holls = []
    for i in range(0, n, n // 2):
        for j in range(0, n, n // 2):
            divided_holl = [row[j:j + n // 2] for row in holl[i:i + n // 2]]
            divided_holls.append((len(divided_holl), divided_holl))

    divided_holls.sort()  # 각 부분행렬을 크기순으로 정렬

    # 가장 작은 부분행렬을 선택하여 재귀호출
    result = devide_conquer(n // 2, divided_holls[0][1])

    return result

n = int(input())
holl = [list(map(int, input().split())) for _ in range(n)]

min_val = devide_conquer(n, holl)
print(min_val)
