n, k = map(int, input().split())
l_a = []
l_b = []
l_a.extend(list(map(int, (input().split()))))
l_b.extend(list(map(int, (input().split()))))
l_a.sort()
l_b.sort(reverse=True)
for i in range(k):
    if l_a[i] < l_b[i]:
        l_a[i], l_b[i] = l_b[i], l_a[i]
    else:
        break
print(sum(l_a))
