l1 = []
for _ in range(int(input())):
    data = input().split()
    l1.append((data[0], int(data[1])))

l1.sort(key=lambda s: s[1])
for i in l1:
    print(i[0], end=" ")
