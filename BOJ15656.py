from functools import reduce
N, M = map(int,input().split())
nums = list(map(int, input().split()))
nums.sort()

def print_numbers(to_print, count):
    if count==1:
        print(reduce(lambda x,y:x+" "+str(nums[y]),to_print,"")[1:])
    else:
        for i in range(N):
            print_numbers([*to_print,i], count-1)


for i in range(N):
    print_numbers([i], M)