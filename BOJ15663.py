import collections
import itertools
from functools import reduce
N, M = map(int,input().split())
nums = list(map(int, input().split()))
nums.sort()
answers = set()

for p in itertools.permutations(nums,M):
    answers.add(p)

for answer in sorted(list(answers)):
    print(*answer)