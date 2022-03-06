import collections as cl

n, m, v = map(int, input().split())


def dfs(graph, v, visited):
    if not visited[v]:
        visited[v] = True
        print(v, end=" ")
        for i in graph[v]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = cl.deque([v])
    visited[v] = True
    while queue:
        v1 = queue.popleft()
        print(v1, end=" ")
        for i in graph[v1]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i = i.sort()

visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)
dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)
