dp=[[1]*10 for _ in range(int(input())+1)]
dp[1][0]=0
div = int(1e9)
for i in range(2, len(dp)):
    for j in range(10):
        if j==0 or j==9:
            dp[i][j] = dp[i-1][abs(1-j)] % div
        else:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1] % div
print(sum(dp[-1])%div)

