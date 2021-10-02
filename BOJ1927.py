import heapq

heap = []
for _ in range(int(input())):
    s = int(input())
    if s == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, s)
