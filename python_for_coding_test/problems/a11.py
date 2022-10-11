from collections import deque, defaultdict

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]
directions = defaultdict(lambda: 0)

for _ in range(k):
    row, col = map(int, input().split())
    graph[row - 1][col - 1] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    if c == "L":
        directions[int(x)] = -1
    else:
        directions[int(x)] = 1

snake = deque([(0, 0)])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0
time = 0

while 0 <= snake[0][0] + dx[direction] < n and 0 <= snake[0][1] + dy[direction] < n \
        and (snake[0][0] + dx[direction], snake[0][1] + dy[direction]) not in snake:
    head_x, head_y = snake[0]
    nx, ny = head_x + dx[direction], head_y + dy[direction]

    if graph[nx][ny] == 1:
        graph[nx][ny] = 0
    else:
        snake.pop()

    snake.appendleft((nx, ny))

    time += 1
    direction = (direction + directions[time]) % 4

print(time + 1)
