n, m = map(int, input().split())  # 3~50
posX, posY, toward = map(int, input().split())
mapInfo = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited[posX][posY] = 1


def turn_left():
    global toward
    toward -= 1
    if toward == -1:
        toward = 3


count = 1
turn_time = 0

while True:
    turn_left()
    nx = posX + dx[toward]
    ny = posY + dy[toward]

    if visited[nx][ny] == 0 and mapInfo[nx][ny] == 0:
        visited[nx][ny] = 1
        posX = nx
        posY = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = posX - dx[toward]
        ny = posY - dy[toward]

        if mapInfo[nx][ny] == 0:
            posX = nx
            posY = ny
        else:
            break
        turn_time = 0

print(count)
