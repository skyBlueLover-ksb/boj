n = int(input())
INF = int(1e9)
dp = [INF] * (n + 1)
dp2 = [INF] * (n + 1)
dp[0] = 1
dp2[0] = 2
dp[1] = 2
dp2[1] = 6
dp[2] = 7
dp2[2] = 20
dp[3] = 22
dp2[3] = 64
for i in range(4, n + 1):
    dp[i] = (2 * dp[i - 1] + 3 * dp[i - 2] + dp2[i - 3]) % 1000000007
    dp2[i] = dp2[i - 1] + 2 * dp[i]
print(dp[n])
