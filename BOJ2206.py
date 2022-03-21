from collections import deque
N,M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
dist = [list([1e9, 1e9] for _ in range(M)) for __ in range(N)]

def bfs():
    q = deque()
    q.append((0,0))
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    dist[0][0][0] = 1
    dist[0][0][1] = 1
    while q:
        x,y = q.popleft()
        if x == N-1 and y == M-1:
            return min(dist[x][y][0], dist[x][y][1])
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny]==0:
                if dist[nx][ny][0] > dist[x][y][0]+1:
                    dist[nx][ny][0] = dist[x][y][0]+1
                    dist[nx][ny][1] = min(dist[nx][ny][1], dist[x][y][1]+1)
                elif dist[nx][ny][1] > dist[x][y][1]+1:
                    dist[nx][ny][1] = min(dist[nx][ny][1], dist[x][y][1]+1)
                else:
                    continue
                q.append((nx,ny))
            elif graph[nx][ny] == 1:
                if dist[nx][ny][1] > dist[x][y][0]+1:
                    dist[nx][ny][1] = dist[x][y][0]+1
                    q.append((nx, ny))

    return -1
print(bfs())

