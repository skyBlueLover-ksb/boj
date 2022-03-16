def solution(width, height, diagonals):
    # no diagonal
    dp0 = [[0] * (height + 1) for _ in range(width + 1)]
    # with only one diagonal
    dp1 = [[0] * (height + 1) for _ in range(width + 1)]

    for i in range(width + 1):
        for j in range(height + 1):
            if i == 0 or j == 0:
                dp0[i][j] = 1

    for i in range(width + 1):
        for j in range(height + 1):
            if i != 0 and j != 0:
                dp0[i][j] += dp0[i - 1][j] + dp0[i][j - 1]

    for diagonal in diagonals:
        x, y = diagonal[0], diagonal[1]
        dp1[x - 1][y] += dp0[x][y - 1]
        dp1[x][y - 1] += dp0[x - 1][y]

    for i in range(width + 1):
        for j in range(height + 1):
            if i != 0:
                dp1[i][j] += dp1[i - 1][j]
            if j != 0:
                dp1[i][j] += dp1[i][j - 1]

    answer = dp1[width][height] % 10000019
    return answer
