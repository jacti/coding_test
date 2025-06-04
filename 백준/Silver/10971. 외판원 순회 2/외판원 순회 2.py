import sys
# sys.path.append("/Users/jactio/develop/coding_test/function_visualizer")
# sys.stdin = open("input.txt", "r")
# from function_visualizer import FunctionVisualizer
# visualizer = FunctionVisualizer()
input = sys.stdin.readline

INF = float('inf')
N = int(input().rstrip())

# 그래프 읽기: 0은 경로가 없는 것으로 보고 INF 처리
graph = []
for _ in range(N):
    row = list(map(int, input().split()))
    # '0'을 INF로 바꾸기 (자기 자신 대각원을 제외하고 나머지 0은 이동 불가)
    graph.append([INF if x == 0 else x for x in row])

# dp[cur][visited_mask]: 현재 위치가 cur이고, 방문 비트마스크가 visited_mask일 때
# 최소 비용을 저장. visited_mask의 비트 i가 1이면, 노드 i는 이미 방문한 상태.
dp = [[INF] * (1 << N) for _ in range(N)]

# 모든 노드를 다 방문한 상태를 나타내는 마스크
ALL_VISITED = (1 << N) - 1

# @visualizer.visualize(param_names=["cur","n"],show_execution_order=True)
def TSP(cur: int, visited: int) -> int:
    """
    cur: 현재 위치(0 ~ N-1)
    visited: 비트마스크 (예: visited & (1<<i)가 1이면 i번 노드 이미 방문)
    반환값: 현재 cur에서 남은 노드를 모두 방문하고 다시 0번으로 돌아오는 최소 비용
    """
    # 기저 조건: 모든 노드를 다 방문했다면, 출발점(0)으로 돌아가는 비용을 리턴
    if visited == ALL_VISITED:
        # 경로가 없으면 INF를 반환
        return graph[cur][0] if graph[cur][0] != INF else INF

    # 이미 계산된 상태면 바로 반환
    if dp[cur][visited] != INF:
        return dp[cur][visited]

    # 아직 방문하지 않은 노드들을 순회
    for nxt in range(N):
        # 이미 방문한 노드는 건너뛰기
        if visited & (1 << nxt):
            continue
        # 만약 cur → nxt 간선이 없다면 건너뛰기
        if graph[cur][nxt] == INF:
            continue

        next_cost = graph[cur][nxt] + TSP(nxt, visited | (1 << nxt))
        if dp[cur][visited] > next_cost:
            dp[cur][visited] = next_cost

    return dp[cur][visited]


# 0번 노드에서 시작 → visited = (1<<0)로 초기화 (0번 노드만 방문한 상태)
print(TSP(0,1))

# visualizer.render("TSP_DP","png")