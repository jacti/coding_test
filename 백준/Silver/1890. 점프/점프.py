from sys import stdin,setrecursionlimit
setrecursionlimit(100000)
input = stdin.readline

N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

# dp[y][x] == y,x에서 목적지로 갈 수 있는 경우의 수
# dp[y][x] = dp[y+jump][x] + dp[y][x+jump]
dp = [[0]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]

def dfs(y,x):
    global N
    global board
    global dp
    global count

    if visited[y][x]:
        return dp[y][x]
    visited[y][x] = True
    # 점프할 거리
    jump = board[y][x]
    # 보드 안에서 점프가 가능할 때
    for new_y, new_x in ((y+jump,x),(y,x+jump)):
        # 목적지에 도착하면 dp +1
        if new_x == N-1 and new_y == N-1:
            dp[y][x] +=1
        elif 0<=new_y<N and 0<=new_x<N:
            dp[y][x] += dfs(new_y,new_x)
    return dp[y][x]
    
print(dfs(0,0))