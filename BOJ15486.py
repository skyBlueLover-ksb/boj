N = int(input())
dp = [0] * (N + 2)
T = [0] * (N + 1)
P = [0] * (N + 1)
for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

for i in range(1, N + 1):
    if i + T[i] < N + 2:
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])
    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[N + 1])
