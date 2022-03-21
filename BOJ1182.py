N, S = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0

def find_answer(i, total):
    global answer, N, S, numbers
    if total == S:
        answer+=1

    for j in range(i+1,N):
        find_answer(j, total+numbers[j])


for i in range(0,N):
    find_answer(i, numbers[i])

print(answer)