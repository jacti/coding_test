from sys import stdin
# stdin = open("input.txt","r")
input = stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int,input().split()))
    target = int(input())

    dp = [[0]*(target+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i, coin in enumerate(coins):
        i+=1
        for j in range(target+1):
            dp[i][j] = dp[i-1][j]
            if j >= coin:
                dp[i][j] += dp[i][j-coin]
    
    print(dp[-1][-1])