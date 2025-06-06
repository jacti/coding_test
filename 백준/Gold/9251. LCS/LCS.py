from sys import stdin
input = stdin.readline
a_str = input().rstrip()
b_str = input().rstrip()

dp = [[0]*len(a_str) for _ in range(len(b_str))]

for x in range(len(a_str)):
    if b_str[0] == a_str[x]:
        dp[0][x] = 1
    elif x>0:
        dp[0][x] = dp[0][x-1]

for y in range(len(b_str)):
    if a_str[0] == b_str[y]:
        dp[y][0] = 1
    elif y>0:
        dp[y][0] = dp[y-1][0]

for y in range(1,len(b_str)):
    for x in range(1,len(a_str)):
        if a_str[x] == b_str[y]:
            dp[y][x] = dp[y-1][x-1] +1
        else:
            dp[y][x] = max(dp[y-1][x], dp[y][x-1])

print(dp[-1][-1])