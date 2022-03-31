#
#


def solve(k, data):
    dp = [[int(1e9)]*(k) for _ in range(k)]
    dp_2 = [[-1]*(k+1) for _ in range(k+1)]
    def get_sum(start, end):
        if dp_2[start][end] == -1:
            dp_2[start][end] = sum(data[start:end+1])
        return dp_2[start][end]

    for i in range(k):
        dp[i][i] = 0
    dp[0][1] = data[0]+data[1]

    for size in range(k):
        for i in range(k-size):
            for j in range(i,i+size):
                dp[i][i+size] = min(dp[i][i+size], dp[i][j]+dp[j+1][i+size]+get_sum(i, i+size))
    print(dp[0][k-1])

for _ in range(int(input())):
    K = int(input())
    data = list(map(int,input().split()))
    solve(K, data)

