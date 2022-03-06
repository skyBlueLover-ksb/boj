n, m = map(int, input().split())
l1 = []
for _ in range(n):
    l1.append(int(input()))
INF = int(1e9)
dp1 = [INF] * (m + 1)
dp1[0] = 0
for i in range(n):
    for j in range(l1[i], m + 1):
        if dp1[j - l1[i]] != INF:
            dp1[j] = min(dp1[j], dp1[j - l1[i]] + 1)


if dp1[m] > 0:
    print(dp1[m])
else:
    print(-1)
