N = int(input())

dp = [1]*(N+1)
for i in range(2,N+1):
    dp[i] = dp[i-1] + dp[i-2]
    if dp[i] >= 10007:
        dp[i] %=10007

print(dp[N])