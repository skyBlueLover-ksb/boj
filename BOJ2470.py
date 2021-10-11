N = int(input())
array = list(map(int, input().split()))
array.sort()
array2 = list(reversed(array))
i, j = 0, 0
sum = abs(array[i] + array2[j])
i_ans, j_ans = 0, 0
while array[i] < array2[j]:
    mysum = array[i] + array2[j]
    if abs(mysum) < sum:
        sum = abs(mysum)
        i_ans, j_ans = i, j

    if mysum == 0:
        break
    elif mysum < 0:
        i += 1
    else:
        j += 1

print("{} {}".format(array[i_ans], array2[j_ans]))
