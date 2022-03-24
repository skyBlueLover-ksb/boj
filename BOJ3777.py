
dp=[1]*1001
# dp[0]="1"0 - 1
# dp[1]="01"0 - 1
# dp[2]="1001"1 - 2
# dp[3]="0110 1001"1 - 4
# dp[4]="1001 0110 0110 1001"3 - 8
# dp[5]="0110 1001 1001 0110"5 - 16

for i in range(4, 1000):
    dp[i]=dp[i-2]+2**(i-3)

while True:
    try:
        n = int(input())
        print(dp[n])
    except EOFError:
        break