import heapq
N = int(input())
heap = []
for i in range(N):
    heapq.heappush(heap, -int(input()))

for i in range(N-1):
    print(-heapq.heappop(heap), end=" ")

print(-heapq.heappop(heap))

