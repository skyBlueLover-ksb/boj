n = int(input())
dp1 = [0] * (n + 1)
dp1[1] = 1
dp1[2] = 3
for i in range(3, n + 1):
    dp1[i] = (dp1[i - 1] + 2 * dp1[i - 2]) % 796796

print(dp1[n])
