from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
pipe = deque([(0,0), (0,1)])
