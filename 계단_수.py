# 계단 수 -> 외판원 순회 처럼 풀기
import sys
input = sys.stdin.readline

N = int(input())

dp = [[[-1 for _ in range(1<<(10))] for _ in range(10)] for _ in range(N)] 

def travel(i, x, notvisited):
    global N
    if i == N-1:
        dp[i][x][notvisited] = 0 if notvisited != 0 else 1
        return dp[i][x][notvisited]
    if dp[i][x][notvisited] != -1:
        return dp[i][x][notvisited]
    
    dp[i][x][notvisited] = 0
    next_x = []
    if x-1 >= 0:
        next_x.append(x-1)
    if x+1 < 10:
        next_x.append(x+1)
    
    for _x in next_x:
        new_notvisited = notvisited & ~(1<<_x)
        dp[i][x][notvisited] += travel(i+1,_x, new_notvisited)
    
    return dp[i][x][notvisited]

if N <10 :
    print(0)
else :
    n = 0
    for start in range(1,10):
        n += travel(0, start, 0b1111111111 & ~(1 << start))
        n%= 1000000000
    print(n)