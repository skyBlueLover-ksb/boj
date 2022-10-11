N = int(input())
arr = list(map(int, input().split()))
arr.sort()
idx = 0
ans = -1

while idx < N:
    idx += arr[idx]
    ans += 1
print(ans)