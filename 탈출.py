from sys import stdin
from collections import deque
# stdin = open("input.txt","r")
input = stdin.readline

R, C = map(int,input().split())
checked_map = [[False] * C for _ in range(R)]
forest_map = []
D = (0,0)
S = (0,0,0,'dochi')
q = deque()
directions = ((0,1),(0,-1),(1,0),(-1,0))

for y in range(R):
    forest_map.append(list(input().rstrip()))
    for x, t in enumerate(forest_map[-1]):
        if t == 'D':
            D = (y,x)
            continue
        elif t == 'S':
            S = (y,x,0,'dochi')
            continue
        elif t == 'X':
            checked_map[y][x] = True
            continue
        elif t == '*':
            checked_map[y][x] = True
            q.appendleft((y,x,0,'hongsu'))
q.appendleft(S)
flood = False
time = 0
while q:
    current = q.pop()
    if current[3] == 'dochi' and current[0] == D[0] and current[1] == D[1]:
        print(current[2])
        break

    if flood and current[2] > time:
        print("KAKTUS")
        break
    # 다음 자식 탐색
    y, x, time = current[0], current[1], current[2]
    checked_map[y][x] = True
    for dy, dx in directions:
        new_y = y + dy
        new_x = x + dx
        if 0<= new_y <R and 0 <= new_x <C:
            if current[3] == 'dochi':
                flood = False
                if not checked_map[new_y][new_x]:
                    forest_map[new_y][new_x] = time+1
                    q.appendleft((new_y,new_x,time+1,'dochi'))
            else :
                flood = True
                if forest_map[new_y][new_x] != "*" and forest_map[new_y][new_x] != "D" and forest_map[new_y][new_x] != "X":
                    forest_map[new_y][new_x] = "*"
                    checked_map[new_y][new_x] = True
                    q.appendleft((new_y,new_x,time+1,'hongsu'))
else:
    print("KAKTUS")