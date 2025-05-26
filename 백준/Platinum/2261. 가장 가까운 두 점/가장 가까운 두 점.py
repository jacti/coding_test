import sys
from bisect import bisect_left,bisect_right
# sys.stdin = open("input.txt","r")

input = sys.stdin.readline

n = int(input())
dot_list = [tuple(map(int,input().split()))for _ in range(n)]
dot_list.sort(key=lambda x: x[0])

min_distance = float('inf')

def get_distance(dot1:tuple[int,int],dot2:tuple[int,int]):
    return (dot1[0] - dot2[0])**2 + (dot1[1] - dot2[1])**2

def get_min(dot_list:list[tuple[int,int]],start,end):
    if end - start <=3:
        result = float('inf')
        for i in range(start,end):
            for j in range(i+1,end):
                distance =get_distance(dot_list[i],dot_list[j])
                result = distance if distance < result else result
        return result
    else:
        half = (start+end)//2
        half_x = dot_list[half][0]
        distance_left = get_min(dot_list,start,half)
        distance_right = get_min(dot_list,half,end)
        min_distance = min(distance_left,distance_right)

        root_min_distance =min_distance ** 0.5
        l = bisect_left(dot_list,half_x-root_min_distance,start,half,key=lambda dot:dot[0])
        r = bisect_right(dot_list,half_x+root_min_distance,half,end,key=lambda dot:dot[0])
        righ_dots = dot_list[half:r]
        righ_dots.sort(key=lambda dot:dot[1])
        for left_dot in dot_list[l:half]:
            i = bisect_left(righ_dots,left_dot[1]-root_min_distance,key=lambda dot:dot[1])
            while i < len(righ_dots) and left_dot[1] + root_min_distance > righ_dots[i][1]:
                distance = get_distance(left_dot,righ_dots[i])
                if min_distance > distance:
                    min_distance = distance
                i+=1
        return min_distance

print(get_min(dot_list,0,n))
                