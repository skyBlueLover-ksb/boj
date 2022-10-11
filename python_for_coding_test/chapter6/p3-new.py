n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    data.append((name, score))

data.sort(key=lambda x:x[1])

for datum in data:
    print(datum[0], end=" ")