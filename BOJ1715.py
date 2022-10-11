import heapq
N = int(input())
heap = []
ans = 0

for _ in range(N):
    heapq.heappush(heap, int(input()))

while len(heap)>1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    ans += a+b
    heapq.heappush(heap, a+b)
print(ans)