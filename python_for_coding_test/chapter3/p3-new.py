n, m =map(int, input().split())
nums = [min(list(map(int, input().split()))) for _ in range(n)]
print(max(nums))