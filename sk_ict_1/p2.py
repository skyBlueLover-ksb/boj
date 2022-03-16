def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]
    dx = []
    dy = []
    k = 1
    if clockwise:
        i, j = 0, 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        di = 0
        while k != 1 + 1 + n * n // 4:
            answer[i][j] = k
            answer[n - 1 - i][n - 1 - j] = k
            answer[n - 1 - j][i] = k
            answer[j][n - 1 - i] = k
            if answer[i + dx[di]][j + dy[di]] == 0:
                i, j = i + dx[di], j + dy[di]
            else:
                for l in range(5):
                    if l == 4:
                        return answer
                    if answer[i + dx[(di + l) % 4]][j + dy[(di + l) % 4]] == 0:
                        di = (di + l) % 4
                        i, j = i + dx[di], j + dy[di]
                        break
            k += 1


    else:
        i, j = 0, 0
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        di = 0
        while k != 1 + 1 + n * n // 4:
            answer[i][j] = k
            answer[n - 1 - i][n - 1 - j] = k
            answer[n - 1 - j][i] = k
            answer[j][n - 1 - i] = k
            if answer[i + dx[di]][j + dy[di]] == 0:
                i, j = i + dx[di], j + dy[di]
            else:
                for l in range(5):
                    if l == 4:
                        return answer
                    if answer[i + dx[(di + l) % 4]][j + dy[(di + l) % 4]] == 0:
                        di = (di + l) % 4
                        i, j = i + dx[di], j + dy[di]
                        break
            k += 1

    return answer
