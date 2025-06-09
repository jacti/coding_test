from sys import stdin
from collections import deque
# stdin = open("input.txt","r")
input = stdin.readline

N, M = map(int,input().split())
dp = [[float('inf')]*(N+1) for _ in range(150)]
impossible = {int(input()) for _ in range(M)}

if 2 in impossible:
    print(-1)
else:
    q = deque([(2,1,1)])
    dp[1][2] = 1
    while q:
        current, speed, count = q.pop()
        if current == N:
            print(count)
            break
        else:
            for new_speed in range(speed-1,speed+2):
                new_current = current + new_speed
                new_count = count+1
                if new_speed<=0 or new_current > N or new_count >= dp[new_speed][new_current] or new_current in impossible:
                    continue
                else:
                    dp[new_speed][new_current] = new_count
                    q.appendleft((new_current,new_speed,new_count))
    else:
        print(-1)