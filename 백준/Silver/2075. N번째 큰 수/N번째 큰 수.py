from sys import stdin
import heapq
input = stdin.readline

N = int(input())

min_heap = []
for _ in range(N):
    numbers = map(int,input().split())
    for i in numbers:
        if len(min_heap) < N:
            heapq.heappush(min_heap, i)
        elif min_heap[0] < i :
            heapq.heappushpop(min_heap,i)

print(min_heap[0])
