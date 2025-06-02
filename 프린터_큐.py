from sys import stdin
from collections import deque
import heapq

# stdin = open("input.txt","r")
input = stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    paper = list(map(int,input().split()))
    paper = deque(paper)

    priority = []
    for p in paper:
        heapq.heappush(priority,-p)
    
    cnt = 0
    while True:
        now = paper.popleft()
        if -priority[0] == now:
            cnt +=1
            if M == 0:
                print(cnt)
                break
            else:
                heapq.heappop(priority)
                N-=1
        else:
            paper.append(now)
        M-=1
        if M <0:
            M = N-1
    