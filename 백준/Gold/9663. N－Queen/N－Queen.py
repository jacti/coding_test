import sys
N = int(sys.stdin.readline())

low_empty = [[True]*N for _ in range(N+1)]
nw_diagonal_empty = [[True]*(2*N-1) for _ in range(N+1)]
ne_diagonal_empty = [[True]*(2*N-1) for _ in range(N+1)]

def n_queen(i:int):
    if i == N:
        return 1
    else :
        result = 0
        for j in range(N):
            # 행 체크, nw 대각선 체크, ne 대각선 체크
            if low_empty[i][j] and nw_diagonal_empty[i][j-i+N-1] and ne_diagonal_empty[i][i+j]:
                low_empty[i+1] = low_empty[i][:]
                nw_diagonal_empty[i+1] = nw_diagonal_empty[i][:]
                ne_diagonal_empty[i+1] = ne_diagonal_empty[i][:]
                
                low_empty[i+1][j] = False
                nw_diagonal_empty[i+1][j-i+N-1] = False
                ne_diagonal_empty[i+1][i+j] = False
                result += n_queen(i+1)
        return result

print(n_queen(0))
