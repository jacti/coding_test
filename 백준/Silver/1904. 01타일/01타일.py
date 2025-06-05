from sys import stdin
input = stdin.readline

N = int(input())

dp = [0] * (N+2)

dp[1] = 1
dp[2] = 2

k = 3
while k <= N:
    dp[k] = dp[k-1] + dp[k-2]
    if dp[k] >= 15746:
        dp[k] %= 15746
    k+=1

print(dp[N])