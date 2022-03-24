V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered

def iterative_dfs(start_v):
    searched = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in searched:
            searched.append(v)
            for i in range(len(graph[v])):
                stack.append(graph[v][len(graph[v])-i-1])

    return searched

print(recursive_dfs(1,[]))
print(iterative_dfs(1))