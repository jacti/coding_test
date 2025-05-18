import sys
# sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
for _ in range(N):
    count = 0
    score = 0
    for i in sys.stdin.readline().rstrip():
        if i == 'O':
            count+=1
            score+=count
        else:
            count=0
    print(score)