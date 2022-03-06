import collections as cl


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = cl.deque([v])
    visited[v] = True

    while queue:
        v1 = queue.popleft()
        for i in graph[v1]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
