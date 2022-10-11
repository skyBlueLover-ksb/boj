n = int(input())
nums = list(map(int, input().split()))
a, b, c, d = map(int, input().split())

max_num, min_num = -1e9, 1e9


def dfs(now, a, b, c, d):
    global max_num, min_num
    all = a + b + c + d
    if all == 0:
        max_num = max(now, max_num)
        min_num = min(now, min_num)
    else:
        _now = nums[n - all]
        if a > 0:
            dfs(now + _now, a - 1, b, c, d)
        if b > 0:
            dfs(now - _now, a, b - 1, c, d)
        if c > 0:
            dfs(now * _now, a, b, c - 1, d)
        if d > 0:
            if now < 0:
                dfs(-((-now) // _now), a, b, c, d - 1)
            else:
                dfs(now // _now, a, b, c, d - 1)


dfs(nums[0], a, b, c, d)
print(max_num)
print(min_num)
