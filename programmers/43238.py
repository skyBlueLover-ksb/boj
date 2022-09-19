def solution(n, times):
    left, right = min(times), max(times) * n

    while left < right:
        mid = (left + right) // 2

        possible_n = 0
        for time in times:
            possible_n += mid // time
            if possible_n >= n:
                break

        if possible_n < n:
            left = mid + 1
        else:
            right = mid

    return left

n = 6
times = [7, 10]
solution(n, times)