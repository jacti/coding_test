from sys import stdin
from collections import deque
# stdin = open("input.txt","r")
input = stdin.readline
N, K = map(int,input().split())
q = deque()
virus_list = []
start_list = []
for x in range(N):
    virus_list.append(list(map(int,input().split())))
    for y in range(N):
        if virus_list[x][y] != 0:
            start_list.append((virus_list[x][y],x,y,0))

S, X, Y = map(int,input().split())

start_list.sort(key=lambda x : x[0])

for virus in start_list:
    q.appendleft(virus)

while q:
    virus, x, y, time = q.pop()
    if time >= S:
        break
    for new_x, new_y in [(x, y+1),(x, y-1),(x+1, y),(x-1, y)]:
        if 0 <= new_x < N and 0 <= new_y < N:
            if virus_list[new_x][new_y] == 0:
                virus_list[new_x][new_y] = virus
                q.appendleft((virus,new_x,new_y,time+1))

print(virus_list[X-1][Y-1])