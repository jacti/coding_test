#knapsack 으로 풀어보기 -> 누가 필요한질 출력해야해서 포기
import sys

height_list = [int(x) for x in sys.stdin.readlines()]
height_sum = sum(height_list)

find = False
i =0
while(not find):
    a = height_list[i]
    for b in height_list[i+1:]:
        if height_sum - a - b ==100:
            height_list.remove(a)
            height_list.remove(b)
            find =True
            break
    i+=1
height_list.sort()
for a in height_list:
    print(a)