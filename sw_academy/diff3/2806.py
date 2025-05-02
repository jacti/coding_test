import sys
import copy
sys.stdin = open("input.txt", "r")

def update_table_down(bord:list, x, y):
    new_bord = copy.deepcopy(bord)
    size = len(new_bord)
    for i,j in enumerate(range(y+1,size)):
        new_bord[j][x]= False
        if x+i+1<size:
            new_bord[j][x+i+1] = False
        if x-i-1>=0:
            new_bord[j][x-i-1] = False
    return new_bord

def search(bord_list:list, N, y):
    if y == N:
        return 1
    else:
        sum = 0
        for x in range(N):
            if bord_list[y][y][x]:
                bord_list[y+1] = update_table_down(bord_list[y],x,y)
                sum += search(bord_list,N,y+1)
        return sum

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    bord_list = [[[True]*N for _ in range(N)]for _ in range(N+1)]
    result =  search(bord_list, N, 0)
    print(f"#{test_case} {result}")