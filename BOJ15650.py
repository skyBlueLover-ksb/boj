from itertools import combinations, permutations
N, M = map(int,input().split())
for c in list(combinations([i for i in range(1,N+1)], M)):
    print(*c)