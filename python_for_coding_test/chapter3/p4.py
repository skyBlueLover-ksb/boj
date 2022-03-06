n, k = map(int, input().split())
count = 0

while n > 1:
    num = n % k
    if num != 0:
        count += num
        n -= num
        if n == 0:
            count -= 1
            n = 1
    else:
        n = n // k
        count += 1
print(count)
