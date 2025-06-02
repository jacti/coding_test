import sys
A, B, C = map(int,sys.stdin.readline().split())

def mode(A,B,C):
    if B == 1:
        return A%C
    elif B%2 == 0:
        return mode((A*A)%C,B//2,C)
    else:
        return (mode(A%C,B-1,C)*A)%C

print(mode(A,B,C))