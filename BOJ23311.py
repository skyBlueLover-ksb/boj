# import collections
# N = int(input())
# a = list(input().split())
# start = input()
# target = input()
# counter = collections.Counter(target)
# dp = {k:collections.deque() for k in range(1,len(target)+1)}
# dp[1].append(start)
# found=0
#
# for j in range(1,len(target)):
#     while dp[j]:
#         char = dp[j].popleft()
#         if len(char) < len(target):
#             for i in range(len(char)):
#                 c = char[i]
#                 c_prime = a[ord(c)-ord('a')]
#                 # if len(char)==len(target)-1:
#                 #     if c_prime != c and c_prime in target:
#                 #         dp_target_len.add(char[0:i] + c_prime + char[i:])
#                 #         dp_target_len.add(char[0:i + 1] + c_prime + char[i + 1:])
#                 #     dp_target_len.add(char[0:i] + c + char[i:])
#                 # else:
#                 if c_prime != c and c_prime in target:
#                     dp[j + 1].append(char[0:i] + c_prime + char[i:])
#                     dp[j + 1].append(char[0:i + 1] + c_prime + char[i + 1:])
#                 dp[j + 1].append(char[0:i] + c + char[i:])
# # print(dp)
# # print(dp_target_len)
# if target in dp[len(target)]:
#     print('YES')
# else:
#     print('NO')

# import collections
# import sys
# N = int(sys.stdin.readline().rstrip())
# a = list(sys.stdin.readline().rstrip().split())
#
# def to_prime(ch):
#     global a
#     return a[ord(ch)-ord('a')]
#
# start = sys.stdin.readline().rstrip()
# target = sys.stdin.readline().rstrip()
# dp = [set() for _ in range(len(target)+1)]
# dp[len(target)].add(target)
#
#
# for i in range(len(target), 1, -1):
#     for char in dp[i]:
#         for j in range(len(char)):
#             c = char[j]
#             possible=0
#             if j>0:
#                 if to_prime(char[j-1])==c:
#                     possible+=1
#
#             if possible ==0 and j<len(char)-1:
#                 if to_prime(char[j+1])==c:
#                     possible+=1
#
#             if possible>0:
#                 to_find = char[:j]
#                 if j != len(char)-1:
#                     to_find += char[j + 1:]
#                 if to_find not in dp[i-1]:
#                     dp[i-1].add(to_find)
#
# if start in dp[1]:
#     print("YES")
# else:
#     print("NO")
import collections
# import sys
# N = int(sys.stdin.readline().rstrip())
# a = list(sys.stdin.readline().rstrip().split())
#
# def to_prime(ch):
#     global a
#     return a[ord(ch)-ord('a')]
#
# start = sys.stdin.readline().rstrip()
# target = sys.stdin.readline().rstrip()
# dp = set()
# dp.add(target)
#
# char = target
#
# for char in dp:
#     if len(char)==1:
#         break
#     # char = dp.popleft()
#     for j in range(len(char)):
#         c = char[j]
#         possible=0
#         if j>0:
#             if to_prime(char[j-1])==c:
#                 possible+=1
#
#             if possible ==0 and j<len(char)-1:
#                 if to_prime(char[j+1])==c:
#                     possible+=1
#
#             if possible>0:
#                 to_find = char[:j]
#                 if j != len(char)-1:
#                     to_find += char[j + 1:]
#
#                 dp.add(to_find)
#
# if start in dp:
#     print("YES")
# else:
#     print("NO")

# N = int(input())
# arr = list(map(str, input().split()))
#
# start = input()
#
# test = input()
#
#
# def te(test, word):
#     # print(test, word)
#     if not test:
#         return
#     if len(test) == 1:
#         if test[0] == word:
#             print("YES")
#             exit()
#         # else:
#         #     print("NO")
#         #     exit()
#     flag = False
#     for i in range(len(test)):
#         if test[i] == word:
#             if not flag:
#                 flag = True
#                 now = i
#                 te(test[:now], arr[ord(test[i])-97])
#             else:
#                 te(test[now+1:i], arr[ord(test[i])-97])
#                 now = i
#     if not flag:
#         print("NO")
#         exit()
#     te(test[now+1:], arr[ord(test[now])-97])
#
#
# te(test, start)
#
# print("YES")

import collections
import sys

N = int(sys.stdin.readline().rstrip())
a = list(sys.stdin.readline().rstrip().split())


def to_prime(ch):
    global a
    return a[ord(ch) - ord('a')]


start = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()
dp = collections.deque()
c = None
target_ = ""
for i in range(len(target)):
    char = target[i]
    if c is not None and c == target[i]:
        continue
    else:
        target_ += char

dp.append(target_)

while dp:
    if len(dp[0]) == 1:
        break
    char = dp.popleft()
    c = None
    for j in range(len(char)):
        if c is not None and char[j] == c:
            continue
        c = char[j]
        possible = 0
        if j > 0:
            if to_prime(char[j - 1]) == c:
                possible += 1

            if possible == 0 and j < len(char) - 1:
                if to_prime(char[j + 1]) == c:
                    possible += 1

            if possible > 0:
                to_find = char[:j]
                if j != len(char) - 1:
                    to_find += char[j + 1:]

                dp.append(to_find)

if start in dp:
    print("YES")
else:
    print("NO")

N = int(input())
arr = list(map(ord, input().split()))
for i in range(len(arr)):
    arr[i] -= ord("a")
start = ord(input()) - ord("a")
test = list(input())

n = len(test)

for i in range(n):
    test[i] = ord(test[i]) - ord("a")

dp = [[[-1]*26 for _ in range(n)]for _ in range(n)]


def check(i, j, ch):
    if dp[i][j][ch] != -1:
        return dp[i][j][ch]
    if i == j:
        if ch == test[i]:
            dp[i][j][ch] = True
        else:
            dp[i][j][ch] = False
        return dp[i][j][ch]
    if j - i == 1:
        ch1 = test[i]
        ch2 = test[j]
        ch3 = ch
        virus = arr[ch]
        if ch1 == ch3 and ch2 == ch3:
            dp[i][j][ch] = True
        elif ch1 == ch2:
            dp[i][j][ch] = False
        elif ch1 == ch3 and ch2 == virus:
            dp[i][j][ch] = True
        elif ch2 == ch3 and ch1 == virus:
            dp[i][j][ch] = True
        else:
            dp[i][j][ch] = False
        return dp[i][j][ch]
    virus = arr[ch]
    for k in range(i, j):
        if (test[k] != ch and test[k+1] != ch) :
            continue
        if (check(i, k, ch) and check(k+1, j, ch)) or (check(i, k, virus) and check(k+1, j, ch)) or (check(i, k, ch) and check(k+1, j, virus)):
            dp[i][j][ch] = True
            return dp[i][j][ch]
    dp[i][j][ch] = False
    return dp[i][j][ch]


if check(0, n-1, start):
    print("YES")
else:
    print("NO")