import heapq
import collections as cl

heap = []
result = cl.deque()
flag = 0


def ssort(n, number, l1):
    global flag
    global result
    if heap:
        # print(heap)
        x, y = heapq.heappop(heap)
        if n != 0:
            if x != number + 1:
                l1.append((x, y))
                ssort(n - y, x, l1)
            else:
                if heap:
                    x2, y2 = heapq.heappop(heap)
                    l1.append((x2, y2))
                    heapq.heappush(heap, (x, y))
                    ssort(n - y2, x2, l1)
        else:
            flag = 1
            result = cl.deque(l1)
    else:
        flag = 1
        result = cl.deque(l1)


n = int(input())
l1 = list(map(int, input().split()))
for i in set(l1):
    heapq.heappush(heap, (i, l1.count(i)))

heap2 = list(heap)
a, b = heapq.heappop(heap)
heapq.heappush(heap, (a, b))

ssort(n, a, cl.deque())
if flag == 1:
    while result:
        x, y = result.popleft()
        for _ in range(y):
            print(x, end=" ")
else:
    heap = list(heap2)
    ssort(n, a - 1, cl.deque())
    while result:
        x, y = result.popleft()
        for _ in range(y):
            print(x, end=" ")
