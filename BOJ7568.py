l1 = []
n = int(input())
for _ in range(n):
    l1.append(tuple(map(int, input().split())))


def printRank(i):
    count = 1
    for j in range(n):
        if l1[i][0] < l1[j][0] and l1[i][1] < l1[j][1]:
            count += 1
    print(count, end=" ")


for i in range(n):
    printRank(i)
print()
