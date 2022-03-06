import sys

sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
reversed_graph = [[] for _ in range(V + 1)]

for _ in range(E):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    reversed_graph[v2].append(v1)

ordering = []
visited1 = [False] * (V + 1)
visited1[0] = True
visited2 = [False] * (V + 1)
visited2[0] = True
sccs = []


def dfs(g, v, visited, ordering):
    if not visited[v]:
        visited[v] = True
        for i in g[v]:
            dfs(g, i, visited, ordering)
        ordering.append(v)


for i in range(1, V + 1):
    if not visited1[i]:
        dfs(graph, i, visited1, ordering)
print(ordering)

while ordering:
    v = ordering.pop()
    scc = []
    dfs(reversed_graph, v, visited2, scc)
    if scc:
        sccs.append(tuple(sorted(scc)))
sccs.sort(key=lambda x: x[0])
print(len(sccs))
for i in sccs:
    for j in range(len(i)):
        print(i[j], end=" ")
    print(-1)
