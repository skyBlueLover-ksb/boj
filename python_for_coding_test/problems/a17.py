from collections import deque
n, k = map(int, input().split())
graph = []
virus = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((0, graph[i][j], i, j))


target_s, target_x, target_y = map(int, input().split())

virus.sort(key=lambda x: (x[0], x[1]))
q = deque(virus)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    s, virus, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((s+1, virus , nx, ny))

print(graph[target_x-1][target_y-1])

