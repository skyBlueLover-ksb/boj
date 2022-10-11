from collections import Counter
n, m = map(int, input().split())
arr = list(map(int, input().split()))
c = Counter(arr)
ans = 0

for k,v in c.items():
    for k2 in c.keys():
        if k!=k2:
            ans+=v*c[k2]

print(ans//2)