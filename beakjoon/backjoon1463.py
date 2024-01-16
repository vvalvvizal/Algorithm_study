def backtrack(n, count):
    if n == 1:
        global min_count
        min_count = min(min_count, count)
        return

    if count >= min_count:  # 현재까지의 연산 횟수가 최소 횟수보다 크면 종료
        return

    if n % 3 == 0:
        backtrack(n // 3, count + 1)

    if n % 2 == 0:
        backtrack(n // 2, count + 1)
    if n>1:
        backtrack(n - 1, count + 1)

# 입력 받기
n = int(input())
min_count = float('inf')  # 최소 연산 횟수를 무한대로 초기화
backtrack(n, 0)
print(min_count)
