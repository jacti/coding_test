import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    array.sort(reverse=True)
    i = 0
    result = []
    for j in range(10):
        if j%2 == 0:
            result.append(array[i])
            i +=1
        else:
            result.append(array[-i])
    print(f"#{test_case} {' '.join(map(str,result))}")