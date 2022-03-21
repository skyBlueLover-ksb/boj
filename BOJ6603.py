import itertools
import functools
while True:
    nums = input().split()
    num = int(nums[0])
    if num==0:
        break
    nums = list(map(int,nums[1:]))
    for i in list(itertools.combinations(nums,6)):
        print(functools.reduce(lambda x,y:x+" "+str(y),i,"")[1:])
    print()