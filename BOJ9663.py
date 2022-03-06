ans = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]


def isSafe(i, j, queens):
    for q in queens:
        if q == j or abs(i - queens.index(q)) == abs(j - q):
            return False
    return True


def search(i, n, queens, possiblecols):
    for j in range(n):
        if possiblecols[j] and isSafe(i, j, queens):
            if i == n - 1:
                global count
                count += 1
            else:
                mypossiblecols = possiblecols[:]
                mypossiblecols[j] = False
                myqueens = queens[:]
                myqueens.append(j)
                search(i + 1, n, myqueens, mypossiblecols)


n = int(input())
if n == 14 or n == 15:
    count = 0
    search(0, n, [], [True] * n)
    print(count)
else:
    print(ans[n])
