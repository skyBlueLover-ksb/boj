import heapq
import sys

input = sys.stdin.readline

minheap = []


def run(i):
    if i == 0:
        if minheap:
            print(heapq.heappop(minheap)[1])
        else:
            print(0)
    else:
        heapq.heappush(minheap, (abs(i), i))


for _ in range(int(input())):
    run(int(input()))
