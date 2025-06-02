import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

q = deque()
for _ in range(N):
    txt = input().split()
    op = txt[0]
    if op == "push":
        n = int(txt[1])
        q.appendleft(n)
    elif op == "pop":
        try:
            print(q.pop())
        except:
            print(-1)
    elif op == "size":
        print(len(q))
    elif op == "empty":
        print( 1 if len(q) == 0 else 0)
    elif op == "front":
        try:
            print(q[-1])
        except:
            print(-1)
    elif op == "back":
        try:
            print(q[0])
        except:
            print(-1)