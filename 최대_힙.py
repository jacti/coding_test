import sys
# sys.stdin = open("input.txt","r")
input = sys.stdin.readline
import heapq

N = int(input())
h = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(-heapq.heappop(h))
    else:
        heapq.heappush(h,-x)
