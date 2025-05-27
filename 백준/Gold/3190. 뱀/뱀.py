import sys
from collections import deque
# sys.stdin = open("input.txt","r")

input = sys.stdin.readline
N = int(input())
K = int(input())
game_map = [[0]*N for _ in range(N)]
for _ in range(K):
    r, c = map(int,input().split())
    game_map[r-1][c-1] = 1
game_map[0][0] = -1
L = int(input())
move = []
for _ in range(L):
    tmp = input().split()
    tmp[0] = int(tmp[0])
    move.append(tmp)

move_idx = 0
directions = ((0,1),(1,0),(0,-1),(-1,0))
direction_idx = 0
current_direction = (0,1)
snake = deque([(0,0)])
count = 0
while True:
    head = snake[-1]
    next = (current_direction[0]+head[0],current_direction[1]+head[1])
    if not (0 <= next[0] < N) or not (0 <= next[1] < N) or game_map[next[0]][next[1]] == -1:
        break
    else:
        count+=1
        snake.append(next)
        if game_map[next[0]][next[1]] != 1:
            tail = snake.popleft()
            game_map[tail[0]][tail[1]] = 0    
        game_map[next[0]][next[1]] = -1
        
        operation = move[move_idx]
        if operation[0] == count:
            if operation[1] == "L":
                direction_idx += -1
                if direction_idx < 0:
                    direction_idx = 3
            elif operation[1] == "D":
                direction_idx += 1
                if direction_idx > 3:
                    direction_idx = 0
            current_direction = directions[direction_idx]
            move_idx +=1
            if move_idx == L:
                move_idx = L-1
print(count+1)