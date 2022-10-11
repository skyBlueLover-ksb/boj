import itertools
n=int(input())
students = []
teachers = []
walls = []
graph = [[0]*n for _ in range(n)]

def catch_student(i,j):
    for sx,sy in students:
        flag = False
        if sx == i:
            for k in range(min(sy,j)+1, max(sy,j)):
                if graph[sx][k] == 3:
                    flag = True
                    break
            if flag:
                flag = False
            else:
                return True

        if sy==j:
            for k in range(min(sx, i)+1, max(sx, i)):
                if graph[k][sy] == 3:
                    flag = True
                    break
            if flag:
                flag = False
            else:
                return True

    return False


def is_ok():
    for tx, ty in teachers:
        if catch_student(tx,ty):
            return False
    return True


for i in range(n):
    arr = list(input().split())
    for j in range(n):
        if arr[j] == "S":
            students.append((i,j))
            graph[i][j]=1
        elif arr[j] == "T":
            teachers.append((i,j))
            graph[i][j] = 2
        else:
            walls.append((i,j))


flag = False
possibilites = itertools.combinations(walls, 3)

for a,b,c in possibilites:
    graph[a[0]][a[1]] = 3
    graph[b[0]][b[1]] = 3
    graph[c[0]][c[1]] = 3
    if is_ok():
        flag = True
        break
    graph[a[0]][a[1]] = 0
    graph[b[0]][b[1]] = 0
    graph[c[0]][c[1]] = 0

if flag:
    print("YES")
else:
    print("NO")
