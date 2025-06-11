from sys import stdin
input = stdin.readline

N = int(input())
dp = [0]* (N+1)

dp[1] = 1 

for i in range(2,N+1):
    if i-4 > 0:
        dp[i] = max(2*dp[i-3],dp[i-1] +1, dp[i-4]*3, dp[i-5]*4)
    else :
        dp[i] = dp[i-1] +1

print(dp[N])