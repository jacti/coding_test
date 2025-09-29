from sys import stdin

INF = 10000

# stdin = open("input.txt","r")
input = stdin.readline

N, K = map(int,input().split())
electronics = list(map(int,input().split()))
index_map = dict()
for i, e in enumerate(electronics):
    if e in index_map:
        index_map[e].append(i)
    else:
        index_map[e] = [1]

for k in index_map.keys():
    index_map[k].append(INF)


count = 0
multitab = dict()

for e in electronics:
    if e not in multitab and len(multitab) == N:
        count +=1
        max_value = -1
        pop_key = 0
        for k, v in multitab.items():
            if v==INF:
                pop_key = k
                break
            if v > max_value:
                max_value, pop_key = v, k
        del multitab[pop_key]
    
    multitab[e] = index_map[e][index_map[e][0]]
    index_map[e][0] +=1
print(count)
