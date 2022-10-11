import sys
input = sys.stdin.readline
k, n = map(int, input().split())
lines = []
for i in range(k):
    lines.append(int(input()))

h=0
start, end = 1, max(lines)

while start <= end:
    mid = (start+end)//2
    total = 0
    for i in range(k):
        total += lines[i]//mid

    if total >= n:
        h = max(h, mid)
        start = mid + 1
    else:
        end = mid - 1

print(h)