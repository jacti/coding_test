import sys
sys.setrecursionlimit(300000)
# sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
h_map = []
for _ in range(N):
    h_map.append(list(map(int,sys.stdin.readline().split())))

checked = [[False]*N for _ in range(N)]

def check(y:int,x:int,h:int):
    global checked
    global h_map
    global N
    checked[y][x] = True
    if h_map[y][x] > h:
        for new_y, new_x in [(y+1,x),(y,x+1),(y-1,x),(y,x-1)]:
            if new_x <0 or new_x >=N or new_y <0 or new_y >=N:
                continue
            if checked[new_y][new_x]:
                continue
            else:
                check(new_y,new_x,h)

max_cnt = 1
group_cnt = 1
h=0
while group_cnt > 0:
    h+=1
    group_cnt = 0
    checked = [[False]*N for _ in range(N)]
    for y in range(N):
        for x, is_checked in enumerate(checked[y]):
            if is_checked:
                continue
            else:
                if h_map[y][x] <= h:
                    checked[y][x] = True
                    continue
                else:
                    group_cnt +=1
                    check(y,x,h)
    max_cnt = group_cnt if group_cnt > max_cnt else max_cnt

print(max_cnt)

