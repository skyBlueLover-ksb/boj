import collections as cl
import heapq


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def dfs_iter(graph, v):
    stack = [v]
    visit = set()

    while stack:
        node = stack.pop()
        if node not in visit:
            print(node, end=" ")
            visit.add(node)
            for i in range(len(graph[node])-1, -1, -1):
                stack.append(graph[node][i])


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

distance = [INF] * 7 #(n+1)
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
                heapq.heappusth(q, (cost, i[0]))

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False]*9
dfs(graph, 1, visited)
dfs_iter(graph, 1)