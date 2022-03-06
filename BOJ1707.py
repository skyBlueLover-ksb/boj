import collections as cl

K = int(input())


def bfs(g, visited, v, c):
    global flag
    global colors
    q = cl.deque()
    q.append((v, c))
    while q:
        v1, c1 = q.popleft()
        if visited[v1] == False:
            visited[v1] = True
            colors[v1] = c1
            for i in g[v1]:
                q.append((i, -c1))
        elif colors[v1] == -c1:
            flag = 1
            return


for i in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    colors = [0] * (V + 1)
    visited = [False] * (V + 1)
    visited[0] = True
    flag = 0
    for i in range(E):
        v1, v2 = input().split()
        v1 = int(v1)
        v2 = int(v2)
        graph[v1].append(v2)
        graph[v2].append(v1)
    bfs(graph, visited, 1, 1)

    for i in range(1, V + 1):
        if visited[i] == False:
            bfs(graph, visited, i, 1)

    if flag == 0:
        print("YES")
    else:
        print("NO")
