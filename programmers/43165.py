def solution(numbers, target):
    answer = 0
    N = len(numbers)

    def dfs(idx, value):
        nonlocal answer
        if idx == N:
            if value == target:
                answer += 1
            return
        dfs(idx + 1, value + numbers[idx])
        dfs(idx + 1, value - numbers[idx])

    dfs(0, 0)

    return answer