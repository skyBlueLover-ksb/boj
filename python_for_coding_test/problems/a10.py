def solution(key, lock):


    def rotate_90_deg(matrix):
        n = len(matrix)
        new_matrix = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_matrix[j][n-1-i] = matrix[i][j]
        return new_matrix

    def check(new_lock):
        lock_length = len(new_lock)//3
        for i in range(lock_length, lock_length*2):
            for j in range(lock_length, lock_length*2):
                if new_lock[i][j] != 1:
                    return False
        return True

    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4):
        key = rotate_90_deg(key)
        for x in range(n*2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False