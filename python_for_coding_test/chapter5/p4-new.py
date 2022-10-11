from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if not (0<=nx<n and 0<=ny <m):
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] ==1:
                if nx == n-1 and ny == m-1:
                    return graph[x][y]+1
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))

print(bfs(0,0))

