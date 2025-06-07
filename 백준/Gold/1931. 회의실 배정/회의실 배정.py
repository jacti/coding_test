from sys import stdin
input = stdin.readline

N = int(input())
meetings = [tuple(map(int,input().split())) for _ in range(N)]
meetings.sort(key=lambda x : (x[0],x[1]))

current_fin = meetings[0][1]
count = 1

for meeting in meetings[1:]:
    if meeting[0] >= current_fin:
        count+=1
        current_fin = meeting[1]
    elif meeting[1] < current_fin:
        current_fin = meeting[1]

print(count)