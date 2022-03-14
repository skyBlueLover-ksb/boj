import collections as cl
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
                heapq.heappusth(q, (cost, i[0]))