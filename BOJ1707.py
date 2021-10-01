K = int(input())


def dfs(g, v, c):
    global flag
    global colors

    if colors[v] == 0:
        colors[v] = c
        for val in list(set(g[v])):
            dfs(g, val, -c)
    elif colors[v] == -c:
        flag = 1
        return
    else:
        pass


for i in range(K):
    V, E = input().split()
    V = int(V)
    E = int(E)
    graph = [[] for _ in range(V)]
    colors = [0] * V
    flag = 0
    for i in range(E):
        v1, v2 = input().split()
        v1 = int(v1)
        v2 = int(v2)
        graph[v1 - 1].append(v2 - 1)
        graph[v2 - 1].append(v1 - 1)
    dfs(graph, 0, 1)
    while (flag == 0 and 0 in colors):
        dfs(graph, colors.index(0), 1)

    if flag == 0:
        print("YES")
    else:
        print("NO")
