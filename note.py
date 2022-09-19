import collections as cl
from collections import deque
import heapq


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


INF = float('inf')

distance = [INF] * (n+1)

def dijkstra(graph, start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)

        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

indegree = [0]*(v+1)

def topology_sort():
    result=[]
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")

# find cycle & union-find

def find_parent(parent: [], x):
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

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a,b = map(int, input().split())

    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break

    else:
        union_parent(parent, a, b)


# kruskal Algoirthm
def find_parent(parent: [], x):
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

v, e = map(int, input().split())
parent = [i for i in range(v+1)]

edges = []
edges_use_heapq = []
result = 0
use_heapq = False

if not use_heapq:
    for _ in range(e):
        a,b,cost = map(int, input().split())
        edges.append((cost, a,b))

    edges.sort()

    for edge in edges:
        cost, a,b = edge
        if find_parent(parent, a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result += cost

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