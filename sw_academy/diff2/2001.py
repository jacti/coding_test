import sys
sys.stdin = open("input.txt", "r")

def calculate_prefix_sum(arr):
    size = len(arr)
    prefix_sum = [[0]*(size+1) for _ in range(size+1)]
    for i in range(1,size+1):
        for j in range(1,size+1):
            prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + arr[i-1][j-1]
    return prefix_sum

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    number_list = []
    for _ in range(N):
        number_list.append(list(map(int, input().split())))
    prefix_sum = calculate_prefix_sum(number_list)
    filter = set()
    for i in range(N-M+1):
        for j in range(N-M+1):
            filter.add(prefix_sum[i+M][j+M]-prefix_sum[i+M][j]-prefix_sum[i][j+M]+prefix_sum[i][j])

    print(f"#{test_case} {max(filter)}")