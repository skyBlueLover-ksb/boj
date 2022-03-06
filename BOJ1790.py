import math

n, m = map(int, input().split(" "))
ans = -1
offset = 0
for i in range(1, n + 1):
    m -= int(math.log10(i) + 1)
    if m <= 0:
        ans = i
        offset = int(math.log10(i)) + m
        break

if ans < 0:
    print(-1)
else:
    ans = str(ans)
    print(ans[offset])
