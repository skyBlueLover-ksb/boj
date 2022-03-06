import sys

input = sys.stdin.readline
primes = []
for i in range(2, 123456 * 2):
    for j in range(2, round(i ** 0.5) + 1):
        if i % j == 0:
            break
        if j == round(i ** 0.5):
            primes.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        print(1)
        continue
    count = 0
    for prime in primes:
        if prime > n and prime <= 2 * n:
            count += 1
    print(count)
