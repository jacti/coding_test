import sys
input = sys.stdin.readline

N = int(input())

print_array = [[" " for _ in range(N)] for _ in range(N)]


def print_pattern(x,y,n):
    global print_array
    if n == 1:
        print_array[x][y] = '*'
    else:
        n //= 3
        for j in range(3):
            print_pattern(x,y+n*j,n)
        print_pattern(x+n,y,n)
        print_pattern(x+n,y+2*n,n)
        for j in range(3):
            print_pattern(x+2*n,y+n*j,n)


print_pattern(0,0,N)
for x in range(N):
    print("".join(print_array[x]))
