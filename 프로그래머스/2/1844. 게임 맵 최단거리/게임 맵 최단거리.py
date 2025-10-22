from collections import deque
def solution(maps):
    N, M = len(maps), len(maps[0])
    tf_table = list(map(lambda x: [False for _ in x], maps))
    tf_table[0][0] = True
    q = deque([(1,0,0)])
    while q:
        i, r, c = q.popleft()
        for dr, dc in ((0,1),(0,-1),(1,0),(-1,0)):
            nr = r + dr
            nc = c + dc
            if nr == N-1 and nc == M-1:
                return i+1
            
            if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] == 1 and not tf_table[nr][nc]:
                tf_table[nr][nc] = True
                q.append((i+1, nr, nc))
                
    return -1