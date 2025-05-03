import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    array = []
    for _ in range(N):
        array.append(list(map(int, input().split())))
    dp = [[float("inf")]*N for _ in range(N)]
    bfs = [set() for _ in range(2*N-1)]
    bfs[0].add((0,0))
    dp[0][0] = array[0][0]
    for level in range(2*N-1):
        for y,x in bfs[level]:
            if y < N-1:
                new_length = dp[y][x] + array[y+1][x]
                if new_length < dp[y+1][x]:
                    bfs[level+1].add((y+1,x))
                    dp[y+1][x] = new_length
            if x < N-1:
                new_length = dp[y][x] + array[y][x+1]
                if new_length < dp[y][x+1]:
                    bfs[level+1].add((y,x+1))
                    dp[y][x+1] = new_length
    print(f"#{test_case} {dp[N-1][N-1]}")