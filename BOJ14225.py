N = int(input()) #MAX 20
data = list(map(int, input().split()))
checked=[False]*2000000

def dfs(v, sum=0):
    if v < len(data):
        dfs(v+1, sum+data[v])
        dfs(v+1, sum)
    checked[sum]=True
dfs(0,0)

for i in range(1,2000000):
    if not checked[i]:
        print(i)
        break
