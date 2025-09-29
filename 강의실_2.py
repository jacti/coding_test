from sys import stdin
import heapq
# stdin = open("input.txt","r")
input = stdin.readline

N = int(input())
classes = [tuple(map(int,input().split())) for _ in range(N)]
class_alloc = 1
alloc = [(0,1)]

# 시작 시간으로 정렬
classes.sort(key=lambda c : (c[1], -c[2]))

#끝나는 시간을 min heap에 넣고 제일 짧은 값을 root에서 가져옴
#시작 시간과 제일 짧은 끝나는 시간을 비교, 시작시간이 더 일찍 있으면 새 강의실을 추가
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