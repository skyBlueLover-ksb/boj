import bisect
import collections

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort()
boxes.sort()


def calCountsByRange(nums, left_value, right_value):
    r_i = bisect.bisect_right(nums, right_value)
    l_i = bisect.bisect_left(nums, left_value)
    return r_i - l_i


def getNumbers(num):
    number = m
    for i in range(n - 1):
        n1 = calCountsByRange(boxes, cranes[i], cranes[i + 1])
        num.append(n1)
        number -= n1
    num.appendleft(number)
    return num


def getlower(num):  # n개
    for i in range(n):
        num[i] -= 1
        if num[i] < 0:
            if i != n - 1:
                num[i + 1] += num[i]
                num[i] = 0
            else:
                num[i] = 0


count = 0
if cranes[n - 1] < boxes[m - 1]:
    print(-1)
else:
    nums = getNumbers(collections.deque())
    nums.reverse()
    while max(nums) != 0:
        getlower(nums)
        count += 1
    print(count)
