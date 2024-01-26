from collections import deque

# 큐 초기화
queue = deque()

# 큐의 크기와 추출할 숫자의 개수 입력
n, m = map(int, input().split())

# 큐에 원소 추가
for i in range(1, n + 1):
    queue.append(i)

# 이동 횟수를 저장할 변수 초기화
count = 0 

# 추출할 숫자들 입력
pos = list(map(int, input().split()))

# 각 숫자에 대해 이동 횟수 계산
for p in pos:
    # 현재 큐에서의 위치를 찾음
    index = queue.index(p)
    # 왼쪽으로 회전할지 오른쪽으로 회전할지 결정하여 이동 횟수를 더함
    count += min(index, len(queue) - index)
    # 해당 숫자를 큐에서 제거
    queue.rotate(-index) #반대로 회전 
    queue.popleft()

# 결과 출력
print(count)

