from sys import stdin
from collections import deque
# stdin = open("input.txt","r")
input = stdin.readline
N, K = map(int,input().split())
q = deque()
virus_list = []
start_list = []

# virus 입력
for x in range(N):
    virus_list.append(list(map(int,input().split())))
    for y in range(N):
        if virus_list[x][y] != 0:
            #virus 위치 기록 3번째 인덱스는 시간
            start_list.append((virus_list[x][y],x,y,0))

S, X, Y = map(int,input().split())

#virus 순위가 낮은거부터 넣기 위해 정렬
start_list.sort(key=lambda x : x[0])

#q에 넣음
for virus in start_list:
    q.appendleft(virus)

while q:
    virus, x, y, time = q.pop()
    if time >= S:
        break

    #범위가 리스트를 벗어나지 않고, 새로 확장할 곳의 값이 0 이면 확장, 시간 +1
    for new_x, new_y in [(x, y+1),(x, y-1),(x+1, y),(x-1, y)]:
        if 0 <= new_x < N and 0 <= new_y < N:
            if virus_list[new_x][new_y] == 0:
                virus_list[new_x][new_y] = virus
                q.appendleft((virus,new_x,new_y,time+1))

print(virus_list[X-1][Y-1])