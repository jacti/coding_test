import sys
A,B,C = map(int,sys.stdin.readlines())

arr = [0]*10
result = str(A*B*C)

for i in result:
    arr[int(i)]+=1

for i in arr:
    print(i)