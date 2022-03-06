pos = input()
row = int(pos[1])
col = ord(pos[0]) - ord("a") + 1
count = 0

l1 = [-2, +2]
l2 = [-1, +1]

steps = [(x, y) for x in l1 for y in l2] + [(y, x) for x in l1 for y in l2]


for step in steps:
    row_next = row + step[0]
    col_next = col + step[1]

    if 1 <= row_next <= 8 and 1 <= col_next <= 8:
        count += 1
print(count)
