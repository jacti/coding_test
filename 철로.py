from sys import stdin
import heapq

# stdin = open("input.txt","r")

input = stdin.readline
N = int(input())
homes = [sorted(map(int,input().split())) for _ in range(N)]
l = int(input())
homes.sort(key=lambda x: x[1])


max_count = 0

min_q = []
for home in homes:
    heapq.heappush(min_q,home[0])

    limit = home[1] - l
    while len(min_q)>0 and min_q[0] < limit:
        heapq.heappop(min_q)
    max_count = len(min_q) if len(min_q) > max_count else max_count

print(max_count)