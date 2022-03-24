import functools
N, M = map(int,input().split())
nums = list(map(int, input().split()))
nums = list(set(nums))
nums.sort()

def solve(num, start, ans):
    if len(ans)==num:
        print(functools.reduce(lambda x,y:x+" "+str(nums[y]), ans,"")[1:])
        return
    for i in range(start, len(nums)):
        solve(num, i, [*ans, i])

for i in range(len(nums)):
    solve(M, i, [i])
