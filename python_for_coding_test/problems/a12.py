def solution(n, build_frame):
    answer = [[]]
    
    graph = [[0]*(n+1) for _ in range(n+1)]

    def do(frame):
        x,y,a,b = frame
        if a == 0:
            if b== 0:
                graph[x][y] -= 1
                graph[x][y + 1] -= 1





    for frame in build_frame:
        do(frame)

        
    
    

    return answer


n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
               [3, 2, 1, 1]]
result = [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]

build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
               [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
result = [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]]

ans = solution(n, build_frame)

if result == ans:
    print("OK")
else:
    print(ans)
