from sys import stdin
from bisect import bisect_left

# stdin = open("input.txt","r")

input = stdin.readline

def search(arr, a, index):
    if index == len(arr):
        index -= 1
    if arr[index] == a:
        if index == 0:
            return arr[1]
        elif index == len(arr)-1:
            return arr[-2]
        else:
            return arr[index-1] if abs(a +arr[index-1]) < abs(arr[index+1] +a) else arr[index+1]
    else:
        if index == 0:
            return arr[0]
        if arr[index-1] == a:
            return arr[index]
        else:
            return arr[index] if abs(a + arr[index-1]) > abs(a+ arr[index]) else arr[index-1]


N = int(input())
solution_list = list(map(int, input().split()))
solution_list.sort()
min_sum = float('inf')
result = (0,0)

for a in solution_list:
    b_index = bisect_left(solution_list,-a)
    b = search(solution_list, a, b_index)
    if min_sum > abs(a+b):
        min_sum = abs(a+b)
        result = (a,b)

print(" ".join(map(str,result)))