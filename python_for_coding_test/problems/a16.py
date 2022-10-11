n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for _ in range(n)]
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def can_go(x,y):
    if 0<=x<n and 0<=y<m:
        return temp[x][y]==0
    else:
        return False

def dfs(x,y):
    for i in range(4):
        if can_go(x+dx[i], y+dy[i]):
            temp[x+dx[i]][y+dy[i]] = 2
            dfs(x+dx[i], y+dy[i])

def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def solve(count):
    global answer
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2 :
                    dfs(i,j)
        answer = max(answer, get_score())
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                solve(count)
                graph[i][j] = 0
                count -= 1
solve(0)
print(answer)

