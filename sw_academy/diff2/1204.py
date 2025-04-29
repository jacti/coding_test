import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    temp = int(input())
    num_dict = dict()
    max_num, max_count = 0,0
    num_list = list(map(int,input().split()))
    for i in num_list:
        if i not in num_dict:
            num_dict[i] = 1
        else:
            num_dict[i]+=1
        if max_count < num_dict[i]:
            max_num = i
            max_count = num_dict[i]
        elif max_count == num_dict[i]:
            if max_num < i:
                max_num = i
    print(f"#{test_case} {max_num}")