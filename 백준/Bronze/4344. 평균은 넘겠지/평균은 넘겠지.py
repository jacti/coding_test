import sys
C = int(sys.stdin.readline())
for _ in range(C):
    arr = [int(i) for i in map(int,sys.stdin.readline().split())]
    N = arr[0]
    mean_score = sum(arr[1:])/N
    count = 0
    for i in arr[1:]:
        if i > mean_score:
            count+=1
    print(f"{count/N*100:.3f}%")
           