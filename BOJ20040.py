def find_parent(parentlist, x):
    if parentlist[x] != x:
        parentlist[x] = find_parent(parentlist, parentlist[x])
    return parentlist[x]


def union_parent(parentlist, x, y):
    x = find_parent(parentlist, x)
    y = find_parent(parentlist, y)

    if x < y:
        parentlist[y] = x
    else:
        parentlist[x] = y


n, m = map(int, input().split())
parentlist = [-1] * n
for i in range(n):
    parentlist[i] = i

for i in range(m):
    x, y = map(int, input().split())
    if find_parent(parentlist, x) == find_parent(parentlist, y):
        print(i)
        break
    else:
        union_parent(parentlist, x, y)
    if i == m - 1:
        print(0)
