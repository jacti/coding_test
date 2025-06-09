from sys import stdin
from collections import deque

# stdin = open("input.txt","r")

input = stdin.readline

n, k = map(int,input().split())

coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
coins = set(coins)

q = deque()

dp = {}
dp[k] = -1
for coin in coins:
    dp[coin] = 1
    if coin == k:
        q.clear()
        break
    q.appendleft((coin,1))
while q:
    finish = False
    coin_sum, count = q.pop()
    count +=1
    for coin in coins:
        new_coin_sum = coin_sum + coin
        if new_coin_sum == k:
            finish = True
            dp[new_coin_sum] = count
            break
        elif new_coin_sum < k and (new_coin_sum not in dp or dp[new_coin_sum] > count):
            dp[new_coin_sum] = count
            q.appendleft((new_coin_sum,count))
    if finish:
        break

print(dp[k])