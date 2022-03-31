N = int(input())
nums = list(map(int, input().split()))
dp=[1e9]*(N+1)

for i in range(1,N+1):
    dp[i] = min(dp[i], nums[i-1])
    for j in range(1, i):
        dp[i] = min(dp[i], dp[i-j]+dp[j])
print(dp[N])
