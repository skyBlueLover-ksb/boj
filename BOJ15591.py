import sys
import collections as cl
sys.setrecursionlimit(10**5)
N, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(N-1):
    p,q,r = map(int, input().split())
    graph[p].append((q,r))
    graph[q].append((p,r))

# for i in range(1,N+1):
#     for j in range(1,N+1):
#         for k in range(1,N+1):
#             v = min(graph[i][k],graph[k][j])
#             if(graph[i][j] < v):
#                 graph[i][j] = v

def bfs(k, v, ans_list, cnt, visited):
    cnt[0] = cnt[0] + 1
    visited[k] = True
    for i,j in graph[k]:
        if (not visited[i]) and j>=v:
            ans_list.append(i)
    while ans_list:
        j = ans_list.popleft()
        if not visited[j]:
            bfs(j,v,ans_list,cnt,visited)

for _ in range(Q):
    v,k = map(int, input().split())
    cnt = [-1]
    visited=[False]*(N+1)
    ans_list=cl.deque()
    bfs(k,v,ans_list,cnt,visited)
    print(cnt[0])


