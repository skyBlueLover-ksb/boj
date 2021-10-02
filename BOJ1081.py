def getSum(n):
    n_string = str(n)
    count = 0
    for i in range(len(n_string)):
        count += int(n_string[i])
    return count


m, n = map(int, input().split())
count = 0
for i in range(m, n + 1):
    count += getSum(i)
print(count)
