n = int(input())
x, y = 1, 1


def move(plan):
    global x, y
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dic = {'L': 0, 'R': 1, 'U': 2, 'D': 3}

    if 1 <= x + dx[dic[plan]] <= n:
        x += dx[dic[plan]]
    if 1 <= y + dy[dic[plan]] <= n:
        y += dy[dic[plan]]


moves = list(input().split())

for mov in moves:
    move(mov)
print(y, x)
