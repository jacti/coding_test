from sys import stdin
input = stdin.readline

N, M = map(int,input().split())

room = [input().rstrip() for _ in range(N)]
count = 0

# 가로로 배열 전체를 읽으면서 '-' 가 연속되지 않을 때 마다 count +1
for y in range(N):
    flag = False
    for x in range(M):
        if room[y][x] == '-':
            flag = True
        else:
            if flag:
                count +=1
                flag = False
    else:
        if flag:
            count +=1

# 세로로 배열 전체를 읽으면서 '|' 가 연속되지 않을 때 마다 count +1
for x in range(M):
    flag = False
    for y in range(N):
        if room[y][x] == '|':
            flag = True
        else:
            if flag:
                count +=1
                flag = False
    else:
        if flag:
            count +=1
print(count)