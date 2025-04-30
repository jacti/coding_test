# 재귀함수를 이용한 풀이
# i: 집중하고 있는 물건의 index
# W: 담을 수 있는 최대 무게(가격)
# w: 무게 리스트
# p: 가치 리스트
## w, p의 0번째 index는 0으로 초기화 실제 값은 index 1부터 시작
## 각 물건별로 담을지 담지 말지 선택을 반복
def knapsack_recursive(i: int, W: int, w: list, p: list):
    # 종료 조건 index가 범위를 벗어나거나 담을 수 있는 한계가 0 이하
    if i <= 0 or W <= 0:
        return 0

    # 담을 수 있는 한계보다 현재 물품 무게가 무거울 시
    # 이 물건은 담지 않고 다음으로 넘김
    elif W < w[i]:
        skip = knapsack_recursive(i - 1, W, w, p)
        return skip

    # 이 물건을 담는 경우, 담지 않고 다음으로 넘기는 경우 중 price가 높은 경우를 채택
    else:
        skip = knapsack_recursive(i - 1, W, w, p)
        # 한계 무게가 작아지고 현재 물건의 가치만큼 담은 가치가 올라감
        pick = knapsack_recursive(i - 1, W - w[i], w, p) + p[i]
        return max(skip, pick)


# dp를 이용한 풀이
# W: 담을 수 있는 최대 무게
# w: 무게 리스트
# p: 가치 리스트
## w, p의 0번째 index는 0으로 초기화 실제 값은 index 1부터 시작
def knapsack_dp(W: int, w: list, p: list):
    # size == N+1
    size = len(w)
    # dp[i][j] => j 무게 이하로 i index 이하 선택지로 담았을 때 최대 가치
    dp = [[0] * (W + 1) for _ in range(size)]

    # 0부터 채워감
    for i in range(1, size):
        for j in range(W + 1):
            # 남은 무게로 물건을 넣을 수 있을 때
            if j - w[i] > 0:
                # 이 물건을 담았을 때, 담지 않았을 떄 중에 max
                skip = dp[i - 1][j]
                pick = dp[i - 1][j - w[i]] + p[i]
                dp[i][j] = max(skip, pick)
            else:
                # i-1 에서 오류가 안나기 위해 [1,N] 범위에서 저장
                dp[i][j] = dp[i - 1][j]
    # 전체 물품에 대해서 W 무게 이하 최대값
    return dp[size - 1][W]



# 테스트 코드
cli = """\n
    테스트 할 함수 입력:
    1. knapsack_recursive
    2. knapsack_dp
    >> """
T = input(cli)

N, W = 5, 1000
weight_list = [0, 200, 500, 300, 1000, 400]
price_list = [0, 100, 300, 250, 500, 400]

if T == "1":
    print(f"#knapsack_recursive: {knapsack_recursive(N,W,weight_list,price_list)}")
elif T == "2":
    print(f"#knapsack_dp: {knapsack_dp(W,weight_list,price_list)}")
else:
    print("Wrong Input")
