n, m = map(int, input().split())
count = 1

while m != n:
    if m < n:
        count = -1
        break

    if m % 10 == 1:
        m = m // 10
        count += 1
    elif m % 2 == 0:
        m = m // 2
        count += 1
    else:
        count = -1
        break

print(count)
