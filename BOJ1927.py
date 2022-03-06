import heapq
import sys

input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    s = int(input())
    if s != 0:
        heapq.heappush(heap, s)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
