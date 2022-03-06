n = int(input())
l1 = list(map(int, input().split()))
l2 = [0] * n
l2[0] = l1[0]
l2[1] = max(l1[0], l1[1])

for i in range(2, n):
    l2[i] = max(l2[i - 1], l2[i - 2] + l1[i])
print(l2[n - 1])
