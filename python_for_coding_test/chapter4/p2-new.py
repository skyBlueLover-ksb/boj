now = input()
moves = []
for i in {1,2}:
    moves.append((i,3-i))
    moves.append((-i, 3 - i))
    moves.append((i, -3 + i))
    moves.append((-i, -3 + i))

now_x = int(now[1])
now_y = ord(now[0]) - ord('a')

ans = 0

for move in moves:
    if 1<=now_x+move[0]<=8 and 1<= now_y+move[1]<=8:
        ans+=1

print(ans)


