N = int(input())
nums = list(map(int, input().split()))
M = int(input())

for i in range(N-1):
    if M == 0:
        break
    max_numi = nums[i]
    max_idx = i
    for j in range(i+1, min(N, i+1+M)):
        if max_numi<nums[j]:
            max_numi = nums[j]
            max_idx = j
    M -= max_idx-i

    for j in range(max_idx, i, -1):
        nums[j] = nums[j-1]
    nums[i] = max_numi
print(*nums)




