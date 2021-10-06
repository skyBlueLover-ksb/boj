n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

ordering = []
visited = [False] * (n + 1)
visited[0] = True


def topologicalOrdering(g, v, visited, ordering):
    if not visited[v]:
        visited[v] = True
        for i in g[v]:
            topologicalOrdering(g, i, visited, ordering)
        ordering.append(v)


for i in range(1, n + 1):
    topologicalOrdering(graph, i, visited, ordering)
ordering.reverse()
print(" ".join([str(ordering[i]) for i in range(len(ordering))]))
