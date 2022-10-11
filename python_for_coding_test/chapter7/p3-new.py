n, m = map(int, input().split())
la = list(map(int, input().split()))
la.sort(reverse=True)
start, end = 0, la[0]

h = 0

while start <= end:
    total = 0
    mid = (start+end) // 2

    for i in range(n):
        if la[i]<=mid:
            break
        else:
            total += la[i]-mid

    if total >= m:
        h = max(h, mid)
        start = mid + 1
    else:
        end = mid-1
print(h)