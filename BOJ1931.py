N = int(input())
schedules = []
possibles = []
for i in range(N):
    a, b = map(int, input().split())
    schedules.append((a, b))
schedules.sort(key=lambda x:(x[1], x[0]))

for sched in schedules:
    if not possibles:
        possibles.append(sched)
    elif possibles and sched[0]>=possibles[-1][1]:
        possibles.append(sched)
print(len(possibles))

