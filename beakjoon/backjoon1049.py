# 패키지와 개별 항목의 비용을 저장할 리스트 초기화
package = []
each = []

# 입력 받기
n, m = map(int, input().split())
for _ in range(m):
    p, e = map(int, input().split())
    package.append(p)
    each.append(e)

# 패키지와 개별 항목의 비용을 오름차순으로 정렬
package.sort()
each.sort()

# 필요한 돈의 최솟값을 저장할 변수 초기화
total_cost = 0

# 패키지와 낱개 중 더 저렴한 것을 선택하여 구매
while n > 0:
        if n >= 6:
            if package[0] <= each[0] * 6:
                total_cost += package[0]
                n -= 6
            else:
                total_cost += each[0] * n
                n = 0
        elif n < 6:
            if each[0] * n <= package[0]:
                total_cost += each[0] * n
                n = 0
            else:
                total_cost += package[0]
                n -= 6

        else:
            total_cost += package[0]
            n -= 6

print(total_cost)
