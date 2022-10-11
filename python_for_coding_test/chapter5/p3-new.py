n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]


def dfs(x, y):
    if 0 <= x < n and 0 <= y < m:
        if graph[x][y] == 0:
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            return True
    else:
        return False


ans = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            ans += 1
print(ans)
