def countZero(num):
    myStr = str(num)
    count = 0
    for i in range(len(myStr)):
        if myStr[i] == "0":
            count += 1
    return count


for _ in range(int(input())):
    n, m = map(int, input().split())
    count = 0
    for i in range(n, m + 1):
        count += countZero(i)
    print(count)
