from collections import deque
N = int(input())
K = int(input())

def direction_change(d,c):
    if c=="L":
        d = (d-1)%4
    else:
        d = (d+1)%4
    return d

board = [[0]*N for _ in range(N)]
for _ in range(K):
    x,y = map(int, input().split())
    board[x-1][y-1] = 1
L = int(input())
times = {}

for i in range(L):
    x, c = input().split()
    times[int(x)] = c

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direction = 1
time = 1
x, y = 0, 0
snake = deque([[x,y]])
board[x][y] = 2

while True:
    x,y = x+dx[direction], y+dy[direction]
    if 0<=x<N and 0<=y<N and board[x][y]!=2:
        if not board[x][y] == 1:
            delX, delY = snake.popleft()
            board[delX][delY] = 0
        board[x][y] = 2
        snake.append([x,y])
        if time in times.keys():
            direction = direction_change(direction,times[time])
        time += 1
    else:
        break
print(time)

