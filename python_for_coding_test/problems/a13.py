def get_distance(chicken):
    sum_distances = []
    for h in house:
        min_dis = 987654321
        for c in chicken:
            dis = abs(h[0] - c[0]) + abs(h[1] - c[1])
            min_dis = min(min_dis, dis)
        sum_distances.append(min_dis)
    return sum_distances


def solve(idx, x, y):
    global answer
    if idx == M:
        choice_chicken = []
        for i in range(N):
            for j in range(N):
                if city[i][j] == 3:
                    choice_chicken.append((i, j))
        res = get_distance(choice_chicken)

        if answer > sum(res):
            answer = sum(res)

        return
    else:
        for i in range(x, N):
            if i == x:
                k = y
            else:
                k = 0
            for j in range(k, N):
                if city[i][j] == 2:
                    city[i][j] = 3
                    solve(idx + 1, i, j + 1)
                    city[i][j] = 2

N, M = map(int, input().split())
answer = 987654321
city = [list(map(int, input().split())) for _ in range(N)]
house = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
solve(0, 0, 0)
print(answer)

