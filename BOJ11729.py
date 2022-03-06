l1 = []


def hanoi(n, a, b):  # n개를 a에서 b로 이동
    if n == 1:
        l1.append((a, b))
    else:
        hanoi(n - 1, a, 6 - a - b)
        hanoi(1, a, b)
        hanoi(n - 1, 6 - a - b, b)


hanoi(int(input()), 1, 3)
print(len(l1))
for i in l1:
    print("{} {}".format(i[0], i[1]))
