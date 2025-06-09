from sys import stdin

input = stdin.readline

N = int(input().rstrip())
homes = [input().rstrip() for _ in range(N)]
checked_map = [[False]*N for _ in range(N)]
count_list = []

def clustering(y,x):
    global N
    global homes
    global checked_map
    directions = ((0,1),(0,-1),(1,0),(-1,0))

    count = 1
    checked_map[y][x] = True

    # 상하좌우에서 범위가 리스트를 안 벗어나고, 이전에 체크를 안한 '1' 이면 확장
    for new_y, new_x in [(y+dy,x+dx) for dy,dx in directions]:
        if 0 <= new_y < N and 0 <= new_x < N :
            if homes[new_y][new_x] == '1' and not checked_map[new_y][new_x]:
                # 재귀적으로 확장한 자식들의 갯수를 리턴받아서 합침
                count += clustering(new_y, new_x)
    return count

for y in range(N):
    for x in range(N):
        if homes[y][x] == '1' and not checked_map[y][x]:
            count_list.append(clustering(y,x))

print(len(count_list))
count_list.sort()
print(*count_list, sep= "\n")