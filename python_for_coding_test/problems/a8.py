from collections import deque
s = list(input())
s.sort()
s = deque(s)
sums = 0

while s[0].isdigit():
    sums += int(s.popleft())
s.append(str(sums))
print("".join(s))
