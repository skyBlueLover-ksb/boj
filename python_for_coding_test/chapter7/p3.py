n, m = map(int, input().split())
list_0 = list(map(int, input().split()))

start = 0
end = max(list_0)
result = -1
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in list_0:
        if i > mid:
            total += i - mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
