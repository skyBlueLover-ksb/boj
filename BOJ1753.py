import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
INF = int(1e9)
graph = [[] for _ in range(V + 1)]
distance_from_start = [INF] * (V + 1)
distance_from_start[start] = 0
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
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


dijkstra(start)
for i in range(1, V + 1):
    val = distance_from_start[i]
    if val == INF:
        print("INF")
    else:
        print(val)
