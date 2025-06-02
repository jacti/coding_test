import sys
# sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
circles = []
for _ in range(N):
    x, r = map(int,input().split())
    circles.append((x-r,'start'))
    circles.append((x+r,'end'))
circles.sort(key=lambda c: (c[0],c[1]))
stack = []
area_count = N+1

for circle in circles:
    if circle[1] == 'start':
        stack.append(circle)
    else:
        area = 0
        while stack[-1][1] != 'start':
            num = stack.pop()
            area += num[0]
        start = stack.pop()
        if area == circle[0] -start[0]:
            area_count +=1
        stack.append((circle[0] -start[0],'area'))
print(area_count)


