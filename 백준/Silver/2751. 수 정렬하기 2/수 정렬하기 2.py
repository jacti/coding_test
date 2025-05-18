import sys

N = int(sys.stdin.readline())

array = [int(i) for i in sys.stdin.readlines()]
array.sort()
for i in array:
    print(i)