import sys
N = int(sys.stdin.readline())
A = set(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int,sys.stdin.readline().split()))

for i in check:
    if i in A:
        print(1)
    else:
        print(0)