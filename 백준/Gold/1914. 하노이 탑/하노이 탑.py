import sys
N = int(sys.stdin.readline())

move = []
def hanoi(n,org ,des):
    global move
    if n == 1:
        move.append((org,des))
    else:
        s1 = set([1,2,3])
        s2 = set([org,des])
        rest = (s1 - s2).pop()
        hanoi(n-1,org,rest)
        move.append((org,des))
        hanoi(n-1,rest,des)

count = [-1]*(N+1)
count[1] = 1
def hanoi_20(n):
    global count
    if count[n] != -1:
        return count[n]
    else:
        count[n] = 2*hanoi_20(n-1) +1
        return count[n]

if N <= 20:
    hanoi(N,1,3)
    print(len(move))
    for org, des in move:
        print(f"{org} {des}")
else:
    print(hanoi_20(N))