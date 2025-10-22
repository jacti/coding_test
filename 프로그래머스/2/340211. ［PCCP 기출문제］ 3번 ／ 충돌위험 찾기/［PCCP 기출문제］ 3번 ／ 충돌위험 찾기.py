from collections import deque

def solution(points, routes):
    def move(s, d):
        if s == d:
            return None
        r1, c1 = s
        r2, c2 = d
        if r1 != r2:
            r1 = r1+1 if r1 < r2 else r1 - 1
        else :
            c1 = c1+1 if c1 < c2 else c1 - 1
        return (r1, c1)
    
    def get_point(i):
        return tuple(points[i-1])
    
    moving = deque((0, get_point(route[0]), i, 1) for i, route in enumerate(routes))
    step = 0
    count = 0
    while moving:
        cur = {}
        while moving and moving[0][0] == step:
            _, c, i, dest = moving.popleft()
            
            if c in cur:
                if not cur[c]:
                    count +=1
                    cur[c] = True
                # print(step+1, i, c, count)
            else:
                cur[c] = False
                    
            nxt = move(c,get_point(routes[i][dest]))
            if nxt == None:
                if dest < len(routes[i]) -1:
                    dest +=1
                    nxt = move(c,get_point(routes[i][dest]))
                            
            if nxt != None:
                moving.append((step+1, nxt, i, dest))
        step += 1
        # print("백준 허브 연동 테스트2")
    return count