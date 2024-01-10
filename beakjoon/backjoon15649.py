def backtrack(candidates, m):
    result = []

    def dfs(i, current):
        if len(current) == m:
            result.append(current.copy())
            return

        if i >= len(candidates):
            return

        current.append(candidates[i])
        dfs(i + 1, current)
        current.pop()
        dfs(i + 1, current)

    dfs(0, [])
    return result

candidates = []
n, m = map(int, input().split())
for i in range(1, n + 1): 

result = backtrack(candidates, m)
print(result)
