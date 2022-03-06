m, n = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


count = 0
for i in range(m):
    for j in range(n):
        if dfs(i, j):
            count += 1
print(count)
