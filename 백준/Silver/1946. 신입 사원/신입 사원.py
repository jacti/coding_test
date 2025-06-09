from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    candidates = [tuple(map(int,input().split())) for _  in range(N)]
    candidates.sort(key=lambda x: x[0])
    count = 1
    base_rank = candidates[0][1]

    for _, rank in candidates[1:]:
        if rank <base_rank:
            count +=1
            base_rank = rank
    
    print(count)
