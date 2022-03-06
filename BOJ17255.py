count = 0


def calc(n, num):
    global count
    if n >= 10:
        if n // 10 == n % (10 ** num):
            calc(n // 10, num - 1)
        else:
            calc(n // 10, num - 1)
            calc(n % (10 ** num), num - 1)
    else:
        if n == 0:
            count += 1
        else:
            count += num + 1


m = input()
n = len(m)
m = int(m)
if m == 0:
    print(1)
else:

    calc(m, n - 1)
    print(count)
