# import sys
# sys.stdin = open("input.txt", "r")


W, H = map(int,input().split())
N = int(input())
arr = [[0] for _ in range(2)]
for _ in range(N):
    is_vertex, i = map(int,input().split())
    arr[is_vertex].append(i)
arr[0].sort()
arr[0].append(H)
arr[1].sort()
arr[1].append(W)
max_area = 0
for i in range(1,len(arr[0])):
    h = arr[0][i] - arr[0][i-1]
    for j in range(1,len(arr[1])):
        area = h * (arr[1][j] - arr[1][j-1])
        max_area = area if area > max_area else max_area
print(max_area)