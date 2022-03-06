x = int(input())
INF = int(1e9)
l1 = [INF] * (x + 1)
l1[1] = 0

for i in range(2, x + 1):
    l1[i] = l1[i - 1] + 1
    if i % 2 == 0:
        l1[i] = min(l1[i], l1[i // 2] + 1)
    if i % 3 == 0:
        l1[i] = min(l1[i], l1[i // 3] + 1)
    if i % 5 == 0:
        l1[i] = min(l1[i], l1[i // 5] + 1)

print(l1[x])
