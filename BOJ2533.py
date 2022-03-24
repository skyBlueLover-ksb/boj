import collections, sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
dp= [[0,0] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(v):
    visited[v]=True
    dp[v][1]=1
    for u in graph[v]:
        if not visited[u]:
            dfs(u)
            dp[v][1] += min(dp[u][0], dp[u][1])
            dp[v][0] += dp[u][1]


dfs(1)
print(min(dp[1][0],dp[1][1]))
