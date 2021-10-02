N = int(input())
map = [[" "] * N for _ in range(N)]


def color(m, n, k):
    if k == 1:
        map[m][n] = "*"
    else:
        for a in range(3):
            for b in range(3):
                if a != 1 or b != 1:
                    color(m + (k // 3) * a, n + (k // 3) * b, k // 3)


color(0, 0, N)
for i in range(N):
    for j in range(N):
        print(map[i][j], end="")
    print()
