from sys import stdin
from bisect import bisect_left
# stdin = open("input.txt","r")

input = stdin.readline

M, N, L = map(int,input().split())

hunters = list(map(int,input().split()))
hunters.sort()

targets = []
for _ in range(N):
    target = tuple(map(int,input().split()))
    if target[1] <= L:
        targets.append(target)


hunter_pos = 0
count = 0

for x,y in targets :
    i = bisect_left(hunters,x)
    if i ==0:
        dx = hunters[i] - x
    elif i == M:
        dx = x - hunters[M-1]
    else:
        dx = min((hunters[i] - x),(x-hunters[i-1]))
    if dx+y <= L:
        count +=1

print(count)
