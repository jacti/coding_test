def solution(triangle):
    dp = [[0]*len(x) for x in triangle]
    def rec(r,c):
        nonlocal dp
        if dp[r][c] != 0:
            return dp[r][c]
        else:
            dp[r][c] = triangle[r][c]
            if r < len(triangle) -1:
                dp[r][c] += max(rec(r+1,c),rec(r+1,c+1))
            return dp[r][c]
    answer = rec(0,0)
    return answer