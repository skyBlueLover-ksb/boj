from itertools import combinations, permutations
N, M = map(int,input().split())
nums = [i+1 for i in range(N)]

def print_numbers(to_print, count):
    if count==1:
        print(to_print)
    else:
        for n in nums:
            print_numbers(str(to_print)+" "+str(n), count-1)


for num in nums:
    print_numbers(num, M)