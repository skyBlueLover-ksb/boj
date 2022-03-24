N, X = map(int, input().split())
data = list(map(int, input().split()))
start = max_days = 0
sum = max_sum = 0
for i, datum in enumerate(data):
    sum += datum
    if i - start + 1 < X:
        continue
    if sum >= max_sum:
        if sum == max_sum:
            max_days += 1
        else:
            max_sum = sum
            max_days = 1
    sum -= data[start]
    start += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(max_days)
