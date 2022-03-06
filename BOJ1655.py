import heapq
import sys
input=sys.stdin.readline

maxheap = []
minheap = []
def heapspush(i):
    if len(maxheap)==len(minheap):
        heapq.heappush(maxheap, (-i,i))
    else:
        heapq.heappush(minheap, (i,i))

    if minheap and maxheap[0][1] > minheap[0][1]:
        left_val=heapq.heappop(maxheap)[1]
        right_val=heapq.heappop(minheap)[1]
        heapq.heappush(minheap,(left_val,left_val))
        heapq.heappush(maxheap,(-right_val,right_val))

    print(maxheap[0][1])
   

for _ in range(int(input())):
    heapspush(int(input()))
