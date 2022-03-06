n = int(input())
l1 = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))


def search(start, end, i):
    mid = (start + end) // 2
    if start > end:
        return False
    num = i - l1[mid]
    if 0 < num:
        return search(mid + 1, end, i)
    elif num < 0:
        return search(start, mid - 1, i)
    else:
        return True


for i in l2:
    if search(0, n - 1, i):
        print("yes", end=" ")
    else:
        print("no", end=" ")
print()
