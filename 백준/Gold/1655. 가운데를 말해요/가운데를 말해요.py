import sys
import heapq

# sys.stdin = open("input.txt","r")

input = sys.stdin.readline

N = int(input())
k = int(input())
print(k)
min_q = []
max_q = [-k]
size_diff = 1
middle = k
for _ in range(N-1):
    k = int(input())
    if k > middle:
        heapq.heappush(min_q,k)
        size_diff -=1

        if size_diff < 0:
            k = heapq.heappop(min_q)
            heapq.heappush(max_q, -k)
            size_diff +=2
    elif k <= middle:
        heapq.heappush(max_q,-k)
        size_diff +=1

        if size_diff >1:
            k = -heapq.heappop(max_q)
            heapq.heappush(min_q, k)
            size_diff -=2
    middle = -max_q[0]
    print(middle)
