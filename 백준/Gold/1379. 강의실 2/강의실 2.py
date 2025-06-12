from sys import stdin
import heapq
# stdin = open("input.txt","r")
input = stdin.readline

N = int(input())
classes = [tuple(map(int,input().split())) for _ in range(N)]
class_alloc = 1
alloc = [(0,1)]

classes.sort(key=lambda c : (c[1], -c[2]))

for k,(i, s, e) in enumerate(classes):
    end_time, j = alloc[0]
    if s>= end_time:
        heapq.heappop(alloc)
        heapq.heappush(alloc,(e,j))
        classes[k] = (i,j)
    else:
        class_alloc+=1
        classes[k] = (i,class_alloc)
        heapq.heappush(alloc,(e,class_alloc))

print(class_alloc)
classes.sort(key=lambda x: x[0])
for _, i in classes:
    print(i)