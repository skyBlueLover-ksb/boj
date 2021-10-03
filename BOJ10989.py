import sys

input = sys.stdin.readline
l1 = [0] * 10001
for _ in range(int(input())):
    l1[int(input())] += 1

for i in range(10001):
    for _ in range(l1[i]):
        print(i)
