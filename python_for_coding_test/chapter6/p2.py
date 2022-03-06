l1 = []
for _ in range(int(input())):
    l1.append(int(input()))
l1.sort(reverse=True)

for i in l1:
    print(i, end=" ")
