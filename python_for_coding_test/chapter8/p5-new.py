n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]
INF = int(1e9)
dp = [INF] * (m+1+max(coins))

for coin in coins:
    dp[coin] = 1

for i in range(1,m+1):
    for coin in coins:
        dp[i+coin] = min(dp[i+coin], dp[i]+1)

if dp[m] != INF:
    print(dp[m])
else:
    print(-1)
