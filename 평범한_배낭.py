from sys import stdin
input = stdin.readline

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

N, K = map(int,input().split())
w = []
p = []
for _ in range(N):
    tmp = tuple(map(int,input().split()))
    w.append(tmp[0])
    p.append(tmp[1])

print(knapsack_dp(K,w,p))

