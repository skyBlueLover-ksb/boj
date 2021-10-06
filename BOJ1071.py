import collections as cl

heap = cl.deque()
result = cl.deque()
n = int(input())
l1 = list(map(int, input().split()))
l1.sort()
for i in set(l1):
    heap.append((i, l1.count(i)))


while heap:
    x1, y1 = heap.popleft()
    if len(heap) != 0:
        x2, y2 = heap.popleft()
        if x1 + 1 < x2:
            result.append((x1, y1))
            heap.appendleft((x2, y2))
        elif x1 + 1 == x2:
            if heap:
                x3, y3 = heap.popleft()
                result.append((x1, y1))
                result.append((x3, 1))
                if y3 != 1:
                    heap.appendleft((x3, y3 - 1))
                heap.appendleft((x2, y2))
            else:
                result.append((x2, y2))
                heap.appendleft((x1, y1))
    else:
        result.append((x1, y1))

while result:
    x, y = result.popleft()
    for _ in range(y):
        print(x, end=" ")
