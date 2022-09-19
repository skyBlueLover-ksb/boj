import sys

input = sys.stdin.readline

tree = [-1] * 3000000
leaf = []


def init(node, start, end):
    if start == end:
        tree[node] = leaf[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
        return tree[node]


def sub_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2

    return sub_sum(node * 2, start, mid, left, right) + sub_sum(node * 2 + 1, mid + 1, end, left, right)


def update(node, start, end, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff

    if start != end:
        mid = (start + end) // 2
        update(node * 2, start, mid, index, diff)
        update(node * 2 + 1, mid + 1, end, index, diff)


n, m, k = map(int, input().rstrip().split())

for _ in range(n):
    leaf.append(int(input().rstrip()))

init(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, input().rstrip().split())

    if a == 1:
        diff = c - leaf[b - 1]
        leaf[b - 1] = c
        update(1, 0, n - 1, b - 1, diff)
    elif a == 2:
        print(sub_sum(1, 0, n - 1, b - 1, c - 1))
