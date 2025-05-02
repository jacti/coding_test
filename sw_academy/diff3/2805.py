import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    farm = []
    for _ in range(N):
        farm.append(list(map(int,list(input()))))
    
    result = 0
    half = N//2
    pick_index = [half]
    for y in range(half):
        for x in pick_index:
            result += farm[y][x]
        pick_index.append(half-1-y)
        pick_index.append(half+1+y)
    
    for i, y in enumerate(range(half,N)):
        for x in pick_index[0:N-i*2]:
            result += farm[y][x]
    
    print(f"#{test_case} {result}")