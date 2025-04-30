import sys
sys.stdin = open("input.txt", "r")

def dfs(N):
    array = [[0]*N for _ in range(N)]
    N = len(array)
    def find_next(saved, N, x, y):
        if x+1 !=N and saved[y][x+1] == 0:
            return x+1, y
        elif y+1 !=N and saved[y+1][x] == 0:
            return x, y+1
        elif x-1 >=0 and saved[y][x-1] ==0:
            return x-1, y
        elif y-1 >=0 and saved[y-1][x] ==0:
            return x, y-1
        else:
            return None, None
    
    x,y = 0,0
    i = 0
    while x!=None:
        i+=1
        array[y][x] =i
        x, y = find_next(array,N,x,y)
    return array
    
T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case}")
    N = int(input())
    result = dfs(N)
    
    for row in result:
        print(" ".join(map(str,row)))
