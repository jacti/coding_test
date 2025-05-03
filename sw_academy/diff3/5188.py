import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    array = []
    for _ in range(N):
        array.append(list(map(int, input().split())))
    
    bfs = [[] for _ in range(2*N-1)]
    bfs[0].append((0,0,array[0][0]))
    for level in range(2*N-1):
        for node in bfs[level]:
            if node[0] < N-1:
                bfs[level+1].append((node[0]+1,node[1],node[2]+array[node[0]+1][node[1]]))
            if node[1] < N-1:
                bfs[level+1].append((node[0],node[1]+1,node[2]+array[node[0]][node[1]+1]))
    result = min(bfs[2*N-2],key=lambda x: x[2])[2]
    print(f"#{test_case} {result}")