def solution(n, edges):
    INF = float('inf')
    graph = [[INF]*n for _ in range(n)]
    answer = 0
    for e in edges:
        graph[e[0]][e[1]]=1
        graph[e[1]][e[0]]=1

    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[i][j]+graph[j][k] == graph[i][k]:
                    if i!=j and j!=k and i!=k:
                        answer+=1


    return answer

n = 7
edges = [[0,1],[1,2],[2,3],[3,4],[1,5], [2,6]]
print(solution(n,edges))