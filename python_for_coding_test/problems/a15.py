from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
inf = int(1e9)

answers = []

def bfs(now, k):
    q = deque([(now, 0)])
    visited = [False] * (n + 1)
    while q:
        u, num = q.popleft()
        if not visited[u]:
            visited[u] = True
            if num == k:
                answers.append(u)
            else:
                for v in graph[u]:
                    q.append((v, num+1))

bfs(x, k)

if answers:
    for i in sorted(answers):
        print(i)
else:
    print(-1)