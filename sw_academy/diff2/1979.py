import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))

    result = 0
    for y in range(N):
        count = 0
        for x in range(N):
            if puzzle[y][x] == 0:
                if count == K:
                    result += 1
                count = 0
            else:
                count += 1
        if count == K:
            result += 1

    for x in range(N):
        count = 0
        for y in range(N):
            if puzzle[y][x] == 0:
                if count == K:
                    result += 1
                count = 0
            else:
                count += 1
        if count == K:
            result += 1
    print(f"#{test_case} {result}")
