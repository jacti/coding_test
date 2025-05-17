import sys
N = int(sys.stdin.readline())
count_array = [0 for _ in range(10001)]

while(N>0):
    count_array[int(sys.stdin.readline())] += 1
    N -= 1

for i, count in enumerate(count_array):
    for _ in range(count):
        print(i)
