n = int(input())
l1 = list(map(int, input().split()))
m = int(input())
l2 = list(map(int, input().split()))

l1.sort()


def bi_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if l1[mid] == target:
            return True
        elif l1[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


for i in l2:
    if bi_search(i, 0, n):
        print("yes", end=" ")
    else:
        print("no", end=" ")
