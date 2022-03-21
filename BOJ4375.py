while True:
    try:
        n=int(input())
    except EOFError:
        break

    s="1"
    while True:
        if int(s) % n == 0:
            print(len(s))
            break
        s += "1"
