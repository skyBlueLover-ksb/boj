A, B, V = map(int, input().split())
day = (V - B - 1) // (A - B) + 1
print(day)