import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())

start = 1
INF = int(1e9)
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
v1, v2 = map(int, input().split())


def dijkstra(start, end):
    distance_from_start = [INF] * (V + 1)
    distance_from_start[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        d, v = heapq.heappop(q)
        if distance_from_start[v] < d:
            continue
        for i in graph[v]:
            if distance_from_start[i[0]] > d + i[1]:
                distance_from_start[i[0]] = d + i[1]
                heapq.heappush(q, (d + i[1], i[0]))
    return distance_from_start[end]


d1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, V)
d2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, V)
d = min(d1, d2)
if d >= INF:
    print(-1)
else:
    print(d)
