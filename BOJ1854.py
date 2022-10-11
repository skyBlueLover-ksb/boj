import heapq
n, m, k = map(int, input().split())
distances = [[] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    heapq.heappush(distances[start], 0)

    while q:
        dist, now = heapq.heappop(q)

        for v in graph[now]:
            if len(distances[v[0]])<k:
                heapq.heappush(q, (v[1] + dist, v[0]))
                heapq.heappush(distances[v[0]], -(dist+v[1]))
            elif (dist+v[1]) < -distances[v[0]][0]:
                heapq.heappop(distances[v[0]])
                heapq.heappush(distances[v[0]], -(dist+v[1]))
                heapq.heappush(q, (v[1] + dist, v[0]))
dijkstra(1)

for i in range(1, n+1):
    if k>len(distances[i]):
        print(-1)
    else:
        print(-distances[i][0])


