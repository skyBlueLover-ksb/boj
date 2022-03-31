ans = []
max_ans = 0
for _ in range(int(input())):
    n =int(input())
    ans.append(n)
    max_ans = max(max_ans, n)

dp=[[0,0,0,0] for _ in range(max_ans+1)]
# 1,000,000,009 divide
dp[1] = [1, 1, 0, 0]
dp[2] = [1, 0, 1, 0]
dp[3] = [3, 1, 1, 1]

for i in range(4, max_ans+1):
    for j in range(1, 4):
        dp[i][j] = (dp[i-j][0]-dp[i-j][j]) % (1e9+9)
    dp[i][0] = sum(dp[i][1:])

for an in ans:
    print(int(dp[an][0] % (1e9+9)))