n, m = map(int, input().split())
x,y,dir = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ans = 0


dx = [-1, 0, 1,0]
dy = [0,1,0,-1]
