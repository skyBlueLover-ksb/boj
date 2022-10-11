n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

max_0 = nums[0]
max_1 = nums[1]

cnt = m//(k+1)

ans = max_1 *cnt + max_0 * (m-cnt)
print(ans)