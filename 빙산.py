'''
모든 탐색은 좌에서 우로 첫줄에서 아랫줄로
0. time = 0
1. 시작점(처음으로 만난 0이 아닌 점)을 기록해둠 // 0이 아닌 점 -> 유효점이라 명명, 0인점을 바다라 명명
2. Cnt = 0
3. 시작점에서 출발 체크한 곳은 True로 표시,
4. 네 방향을 살펴서 각 방향별로 바다가 나오면 다음 빙산 지도에서 내 위치를 -1 함
5. 네 방향을 살펴서 유효점이 나오면 True로 표시
6. 재귀가 종료되면 Cnt +1
7. True로 표시 되지 않은 곳중에 처음으로 유효점이 나오는 곳을 탐색
8. 3 - 6 반복
9. Cnt 값을 세어서 2 이상이면 종료 time 출력
10. 아닐 경우 time +=1, 2 - 다시 반복
'''

import sys
# sys.stdin = open("input.txt","r")
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def check_group(cur_bergs:list[list[int]], new_bergs:list[list[int]], check_map:list[list[bool]],r,c):
    global N, M
    direction = [(-1,0),(1,0),(0,-1),(0,1)]
    
    check_map[r][c] = True
    # 상하좌우 0 체크
    for dy, dx in direction:
        new_c = c + dy
        new_r = r + dx
        if new_c <0 or new_r <0 or new_r >= N or new_c >= M:
            continue
        else:
            if cur_bergs[new_r][new_c] <= 0:
                new_bergs[r][c] -= 1
            else:
                if not check_map[new_r][new_c]:
                    check_group(cur_bergs,new_bergs,check_map,new_r,new_c)


N, M = map(int,input().split())

berg = [list(map(int,input().split())) for _ in range(N)]

time = 0
start_point = (0,0)
cnt = 0
while cnt <2:
    cnt = 0
    check_map = [[False]*M for _ in range(N)]
    new_berg = [row[:] for row in berg]
    r,c = start_point
    x = c
    finish = True
    for y in range(r,N):
        while x < M:
            if not check_map[y][x] and berg[y][x] >0:
                finish = False
                cnt+=1
                if cnt ==1:
                    start_point = (y,x)
                else:
                    check_group(berg,new_berg,check_map,y,x)
            x += 1
            
        x = 0
    if finish:
        time = 1
        break
    berg = new_berg
    time +=1
print(time-1)




