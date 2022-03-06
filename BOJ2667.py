import collections as cl

n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int, input().strip())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

d = []


def search(i, j):
    count = 0
    if g[i][j] == 1:
        g[i][j] = 0
        q = cl.deque()
        q.append((i, j))

        while q:
            x, y = q.popleft()
            count += 1
            for k in range(4):
                if (
                    0 <= x + dx[k]
                    and x + dx[k] < n
                    and 0 <= y + dy[k]
                    and y + dy[k] < n
                ):
                    if g[x + dx[k]][y + dy[k]] == 1:
                        g[x + dx[k]][y + dy[k]] = 0
                        q.append((x + dx[k], y + dy[k]))
    return count


for i in range(n):
    for j in range(n):
        z = search(i, j)
        if z != 0:
            d.append(z)

print(len(d))
d.sort()
for i in d:
    print(i)
