import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
count = 0
l1 = []
for _ in range(n):
    l1.append(int(input()))
l1.reverse()

for i in range(n):
    count += k // l1[i]
    k -= l1[i] * (k // l1[i])

print(count)
