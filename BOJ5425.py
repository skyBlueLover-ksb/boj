import math


def mySum(a):
    if a <= 0:
        return 0
    return getSum(a, int(math.log10(a)))


def getSum(a, n):  # 0에서부터 a까지의 합, n+1자리수
    if n == 0:
        return int(a * (a + 1) / 2)
    else:
        b = a // 10 ** n
        return (
            int(b * (b - 1) / 2 * 10 ** n)
            + b * (1 + a % 10 ** n)
            + 1 * mySum(a % 10 ** n)
            + b * mySum(10 ** n - 1)
        )


for _ in range(int(input())):
    n, m = map(int, input().split())
    print(mySum(m) - mySum(n - 1))
