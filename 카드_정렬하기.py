from sys import stdin
import heapq
input = stdin.readline

N = int(input())
cards = []
for _ in range(N):
    heapq.heappush(cards,int(input()))

count = 0
for _ in range(N-1):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    count += a+b
    heapq.heappush(cards,a+b)
print(count)
