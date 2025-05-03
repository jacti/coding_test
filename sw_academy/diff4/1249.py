import sys
sys.stdin = open("input.txt", "r")

def move(dp:list[list[int]], map_info:list[list[int]],stack:set[tuple[int,int]],N, y, x, value):
    # 이후 더 작은 값이 들어왔을 떄 실행 안함
    if value > dp[y][x]:
        return None
    # 최종값보다 이미 큰 경로는 계산 안함
    elif value > dp[N-1][N-1]:
        return None
    else:
        for new_y, new_x in [(y+1,x),(y,x+1),(y-1,x),(y,x-1)]:
            if new_y <N and new_y>=0 and new_x<N and new_x>=0:
                new_value = value + map_info[new_y][new_x]
                if dp[new_y][new_x] > new_value:
                    dp[new_y][new_x] = new_value
                    stack.add((new_y,new_x,new_value))

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    map_info = []
    for _ in range(N):
        map_info.append(list(map(int,list(input()))))
    dp = [[float("inf")]*N for _ in range(N)]
    stack = {(0,0,0)}
    while len(stack) > 0:
        new_stack = set()
        for y,x, value in stack:
            move(dp,map_info,new_stack,N,y,x,value)
        stack = new_stack

    print(f"#{test_case} {dp[N-1][N-1]}")