n = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1
for x in arr:
    if target < x:
        break
    target += x

print(target)

# 현재 상태를 1부터 target-1까지 모두 만들 수 있는 상태
# 그렇다면 target에 새로운 coin만큼 더하면
# 1부터 target-1 , coin~ coin+target-1 만큼 모두 만들 수 있는 상태!
# 즉, target>=coin 이라면 모든 경우를 만들 coin+target-1의 경우를 모두 만들 수 있다
# 따라서, target < coin 이면 break해버린다. 이 때, 처음으로 만들 수 없는 수는 target
