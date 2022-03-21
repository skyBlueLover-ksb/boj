import collections
N = int(input())
a = list(input().split())
start = input()
target = input()
dp = {k:collections.deque() for k in range(len(target))}
dp_target_len=set()
dp[1].append(start)
found=0

for j in range(1,len(target)):
    while dp[j]:
        char = dp[j].popleft()
        if len(char) < len(target):
            for i in range(len(char)):
                c = char[i]
                c_prime = a[ord(c)-ord('a')]
                if len(char)==len(target)-1:
                    if c_prime != c and c_prime in target:
                        dp_target_len.add(char[0:i] + c_prime + char[i:])
                        dp_target_len.add(char[0:i + 1] + c_prime + char[i + 1:])
                    dp_target_len.add(char[0:i] + c + char[i:])
                else:
                    if c_prime != c and c_prime in target:
                        dp[j + 1].append(char[0:i] + c_prime + char[i:])
                        dp[j + 1].append(char[0:i + 1] + c_prime + char[i + 1:])
                    dp[j + 1].append(char[0:i] + c + char[i:])
print(dp)
print(dp_target_len)
if target in dp_target_len:
    print('YES')
else:
    print('NO')