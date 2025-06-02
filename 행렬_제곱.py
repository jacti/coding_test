import sys
# sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N, B = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]

def matrix_multiple(A:list[list[int]],B:list[list[int]], N):
    def unit_square(A:list[list[int]],B:list[list[int]],x,y,N):
        unit_sum = 0
        for i in range(N):
            unit_sum += A[y][i] * B[i][x]
        return unit_sum % 1000
    
    return [[unit_square(A,B,x,y,N) for x in range(N)] for y in range(N)]

def cal (A:list[list[int]], B, N):
    if B == 1:
        for y in range(N):
            for x in range(N):
                A[y][x] %= 1000
        return A
    if B%2 == 0:
        new_A = cal(A,B//2,N)
        return matrix_multiple(new_A,new_A,N)
    else:
        return matrix_multiple(A,cal(A,B-1,N),N)


result = cal(A,B,N)
for row in result:
    print(" ".join(map(str,row)))