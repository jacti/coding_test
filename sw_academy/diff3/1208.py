import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    dump_count = int(input())
    boxs = list(map(int, input().split()))
    height_list = [0]*100

    for height in boxs:
        height_list[height-1] +=1
    
    max_height = max(boxs)-1
    min_height = min(boxs)-1

    for _ in range(dump_count):
        height_list[max_height] -=1
        height_list[min_height] -=1
        height_list[max_height-1] +=1
        height_list[min_height+1] +=1

        if height_list[max_height] ==0:
            max_height -=1
        if height_list[min_height] ==0:
            min_height +=1
        if max_height - min_height <= 1:
            break

    print(f"#{test_case} {max_height-min_height}")