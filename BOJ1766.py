import heapq

heap = []
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    indegree[v2] += 1


ordering = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    v = heapq.heappop(heap)
    ordering.append(v)
    for i in graph[v]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(heap, i)


print(" ".join([str(ordering[i]) for i in range(len(ordering))]))
