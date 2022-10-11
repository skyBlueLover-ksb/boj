import collections, sys
from typing import List
stack = collections.deque()

def do_command(comm:List):
    if comm[0] == "push":
        stack.append(command[1])
    elif comm[0] == "top":
        try:
            print(stack[-1])
        except:
            print(-1)
    elif comm[0] == "size":
        print(len(stack))
    elif comm[0] == "empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif comm[0] == "pop":
        try:
            print(stack.pop())
        except IndexError:
            print(-1)


N = int(sys.stdin.readline())
for i in range(N):
    command = list(sys.stdin.readline().split())
    do_command(command)
