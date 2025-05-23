import sys
# sys.stdin = open("input.txt","r")
N, M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
trees.sort(reverse=True)
prefix_sum = [trees[0]]
for i in range(1,N):
    prefix_sum.append(trees[i]+prefix_sum[i-1])

def cut_tree(h):
    # h의 index 찾음
    global trees
    left, right = 0, len(trees)
    while left < right:
        half = (left + right)//2
        if trees[half] <= h:
            right = half
        else:
            left = half+1

    return prefix_sum[left-1] - h*(left) if left != 0 else 0

bottom, top = 0, trees[0]
while bottom <= top:
    half = (bottom + top)//2
    count = cut_tree(half)
    if count == M:
        print(half)
        break
    elif count < M:
        top = half-1
    else:
        bottom = half+1
else:
    print(top)
