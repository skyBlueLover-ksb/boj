arr = list(map(int, input()))
now = arr[0]
idx = 1
while idx < len(arr):
    new = arr[idx]
    if now > 1 and new > 1:
        now *= new
    else:
        now += new
    idx += 1
print(now)