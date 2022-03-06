s = list(input().split("-"))
n = 0
for j in s[0].split("+"):
    n += int(j)
for i in range(1, len(s)):
    for j in s[i].split("+"):
        n -= int(j)
print(n)
