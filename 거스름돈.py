from collections import deque
n = int(input())

dp = [0] * (n+1)
q = deque([(0,0)])

while q:
    coin, count = q.pop()
    if coin == n:
        print(count)
        break
    else:
        for i in [5,2]:
            new_coin = coin +i
            if new_coin <=n and dp[new_coin]==0:
                dp[new_coin] = count+1
                q.appendleft((new_coin,count+1))
else:
    print(-1)
