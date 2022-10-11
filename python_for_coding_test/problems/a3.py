s = input()
now = s[0]
count = 0
flag = False

for i in range(len(s)):
    if s[i] == now:
        if flag:
            flag = False
        continue
    else:
        if flag:
            continue
        else:
            count += 1
            flag = True

print(count)
