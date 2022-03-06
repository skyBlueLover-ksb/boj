import heapq

n, m, c = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
    x, y, z = map(int, input().split())
    heapq.heappush(graph[x], (z, y))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
