from sys import stdin

# stdin = open("input.txt","r")

input = stdin.readline

M, N, L = map(int,input().split())

hunters = list(map(int,input().split()))
hunters.sort()

targets = []
for _ in range(N):
    target = tuple(map(int,input().split()))
    if target[1] <= L:
        targets.append(target)

targets.sort(key=lambda x: x[0])

hunter_pos = 0
target_pos = 0
count = 0

for x,y in targets :
    if y > L :
        continue

    Minpossiblehunt = x - (L - y)
    Maxpossiblehunt = x + (L - y)

    while hunter_pos < M and hunters[hunter_pos] < Minpossiblehunt:
        hunter_pos += 1

    if hunter_pos < M and hunters[hunter_pos] <= Maxpossiblehunt:
        count += 1

print(count)
