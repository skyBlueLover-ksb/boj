
import itertools

N, M = map(int,input().split())
nums = list(map(int, input().split()))
nums.sort()
answers = set()

for p in itertools.permutations(nums,M):
    answers.add(p)
answers = sorted(list(answers))
for answer in answers:
    to_list = list(answer)
    length = len(to_list)
    for i in range(1,length+1):
        if i==length:
            print(*answer)
            break
        if to_list[i-1]>to_list[i]:
            break