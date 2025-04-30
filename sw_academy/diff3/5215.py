import sys
sys.stdin = open("input.txt", "r")

# 재귀함수를 이용한 구현
def knapsack2_1(i, W, w, p):
    if (i <= 0 or W <= 0):
        return 0
    if (w[i] > W):
        value = knapsack2_1(i - 1, W, w, p)
        return value
    else: # w[i] <= W
        #스킵하는 경우
        left = knapsack2_1(i - 1, W, w, p)
        #챙겨 가는 경우
        right = knapsack2_1(i - 1, W - w[i], w, p)
        return max(left, p[i] + right)

T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    taste_list = [0]
    cal_list = [0]
    for _ in range(N):
        taste, cal = map(int, input().split())
        taste_list.append(taste)
        cal_list.append(cal)
    print(f"#{test_case} {knapsack2_1(N,L,cal_list,taste_list)}")
