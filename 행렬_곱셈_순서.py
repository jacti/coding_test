from sys import stdin
input = stdin.readline

N = int(input())
matrixs = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0

for combine in range(1,N):
    for start in range(0,N-combine):
        end = start + combine
        for i in range(start,end):
            count = dp[start][i] + dp[i+1][end] + matrixs[start][0]*matrixs[i][1]*matrixs[end][1]
            if count < dp[start][end]:
                dp[start][end] = count

print(dp[0][N-1])
            

