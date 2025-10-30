import sys
# sys.stdin = open("스도쿠_input.txt", "r")

input = sys.stdin.readline
N = 9

grid = [list(map(int, input().split())) for _ in range(N)]

# 비트마스크 초기화 (각 줄, 열, 박스)
hor = [0] * N
ver = [0] * N
box = [0] * N
need_fill = []

def get_box_ind(r, c):
    return (r // 3) * 3 + (c // 3)

# 숫자 세팅 함수
def set_number(r, c, v, hor, ver, box):
    new_hor = hor[:]
    new_ver = ver[:]
    new_box = box[:]
    bit = 1 << (v - 1)
    new_hor[r] |= bit
    new_ver[c] |= bit
    new_box[get_box_ind(r, c)] |= bit
    return new_hor, new_ver, new_box

# 초기 마스크 설정
for i in range(N):
    for j in range(N):
        if grid[i][j] == 0:
            need_fill.append((i, j))
        else:
            hor, ver, box = set_number(i, j, grid[i][j], hor, ver, box)

# 백트래킹
def fill_num(index, hor, ver, box):
    if index == len(need_fill):
        return True  # 모두 채움
    
    r, c = need_fill[index]
    used = hor[r] | ver[c] | box[get_box_ind(r, c)]
    
    for v in range(1, 10):
        bit = 1 << (v - 1)
        if not (used & bit):  # 해당 숫자 사용 가능
            new_hor, new_ver, new_box = set_number(r, c, v, hor, ver, box)
            grid[r][c] = v
            if fill_num(index + 1, new_hor, new_ver, new_box):
                return True
            grid[r][c] = 0  # 복구
    return False

# 실행
fill_num(0, hor, ver, box)

# 출력
for row in grid:
    print(" ".join(map(str, row)))
