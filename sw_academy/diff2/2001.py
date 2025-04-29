import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    number_list = []
    for _ in range(N):
        number_list.append(list(map(int, input().split())))
    row_filter = [[0]*(N-M+1) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            if j==0:
                for k in range(M):
                    row_filter[i][0] += number_list[i][k]
            else:
                row_filter[i][j] = row_filter[i][j-1] - number_list[i][j-1] + number_list[i][j+M-1]
    filter = [[0]*(N-M+1) for _ in range(N-M+1)]
    for j in range(N-M+1):
        for i in range(N-M+1):
            if i==0:
                for k in range(M):
                    filter[0][j] += row_filter[k][j]
            else:
                filter[i][j] = filter[i-1][j] - row_filter[i-1][j] + row_filter[i+M-1][j]
    print(f"#{test_case} {max(map(max,filter))}")