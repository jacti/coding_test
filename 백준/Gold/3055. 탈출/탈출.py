from sys import stdin
from collections import deque

input = stdin.readline

R, C = map(int, input().split())
forest_map = []
water_q = deque()
dochi_q = deque()

directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

for y in range(R):
    row = list(input().rstrip())
    forest_map.append(row)
    for x, t in enumerate(row):
        if t == 'S':
            dochi_q.append((y, x, 0))
        elif t == '*':
            water_q.append((y, x))
            
while True:
    # 1. 물 먼저 확장
    for _ in range(len(water_q)):
        y, x = water_q.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and forest_map[ny][nx] == '.':
                forest_map[ny][nx] = '*'
                water_q.append((ny, nx))

    # 2. 도치 이동
    moved = False
    for _ in range(len(dochi_q)):
        y, x, time = dochi_q.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C:
                if forest_map[ny][nx] == 'D':
                    print(time + 1)
                    exit()
                if forest_map[ny][nx] == '.':
                    forest_map[ny][nx] = 'S'
                    dochi_q.append((ny, nx, time + 1))
                    moved = True
    if not dochi_q:
        break

print("KAKTUS")
