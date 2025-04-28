import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split()))
    buffer = [[0, 0] for _ in range(2)]
    index = 0
    result = 0
    for building in buildings:
        # 후보군 체크
        if buffer[index][0]> building:
                result += min(buffer[index][0] - building, buffer[index][1])
                buffer[index][0] = building
                buffer[index][1] = 0
        else:
            buffer[index][1] = min(building - buffer[index][0], building - buffer[1-index][1])
            buffer[index][0] = building

            
        