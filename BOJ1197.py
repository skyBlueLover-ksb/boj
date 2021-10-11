def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
parent = [0] * (V + 1)
for i in range(1, V + 1):
    parent[i] = i

E_list = []
for _ in range(E):
    a, b, c = map(int, input().split())
    E_list.append((c, a, b))

E_list.sort(key=lambda x: x[0])

count = 0
for item in E_list:
    c, a, b = item
    if find_parent(parent, a) != find_parent(parent, b):
        count += c
        union_parent(parent, a, b)

print(count)
