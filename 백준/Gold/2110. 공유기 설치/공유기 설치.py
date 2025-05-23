import sys
# sys.stdin = open("input.txt","r")
N, C = map(int,sys.stdin.readline().split())
homes = [int(sys.stdin.readline()) for _ in range(N)]
homes.sort()

right = (homes[-1] - homes[0])//(C-1)
left = 1

def binarySearch(arr, target,left,right):
    if left > right:
        return left
    mid = (left+right)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] <target:
        return binarySearch(arr,target,mid+1,right)
    else:
        return binarySearch(arr,target,left,mid-1)

while left <= right:
    p = (left+right)//2
    new_left = 0
    new_right = N-1
    i= 0
    for _ in range(C-1):
        i = binarySearch(homes,homes[i]+p,new_left,new_right)
        if(i>=N):
            break
        new_left = i+1
    if i >= N:
        right = p-1
    else:
        left = p+1

print ((left+right)//2)
    




# def binarySearch(func, target,left,right):
#     if left > right:
#         return right
#     mid = (left+right)//2
#     if func(mid) == target:
#         return mid
#     elif func(mid) <target:
#         return binarySearch(func,target,left,mid-1)
#     else:
#         return binarySearch(func,target,left+1,right)

