n, k = map(int, input().split())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

idx_a = 0
idx_b = 0

list_a.sort()
list_b.sort(reverse=True)

ans = 0

for i in range(k):
    if list_a[i] < list_b[i]:
        list_a[i], list_b[i] = list_b[i], list_a[i]
    else:
        break
print(sum(list_a))

