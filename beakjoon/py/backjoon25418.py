from collections import deque

def min_count_bfs(A, K):
    visited = [False] * (K * 2)  # K*2를 해주는 이유는 A가 1 이상이고 K가 A보다 커야하므로 최대 K*2까지 가능
    queue = deque([(A, 0)])  # (현재 수, 연산 횟수)를 저장하는 큐
    visited[A] = True

    while queue:
        current, count = queue.popleft()

        if current == K:
            return count

        # 1을 더하는 연산
        next_num = current + 1
        if next_num < len(visited) and not visited[next_num]:
            queue.append((next_num, count + 1))
            visited[next_num] = True

        # 2를 곱하는 연산
        next_num = current * 2
        if next_num < len(visited) and not visited[next_num]:
            queue.append((next_num, count + 1))
            visited[next_num] = True


A, K = map(int, input().split())
print(min_count_bfs(A, K))
