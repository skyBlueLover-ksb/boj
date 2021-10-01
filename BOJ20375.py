"""
def f1(a):
    sum = 0
    for i in range(int((a+2) / 3), int(a/2)+1):
        sum += f2(i, a - i)
    return sum


def f2(max, num):
    k = 2 * max - num
    if k < 0:
        return 0
    elif k == 0:
        return 1
    else:
        return int(k / 2) + 1


n = int(input())
print(f1(n))

"""
import itertools
