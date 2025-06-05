from sys import stdin
input = stdin.readline

N, M = map(int,input().split())

room = [input().rstrip() for _ in range(N)]
count = 0
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