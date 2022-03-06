n, m = map(int, input().split())
data = [min(list(map(int, input().split()))) for i in range(n)]
print(max(data))
