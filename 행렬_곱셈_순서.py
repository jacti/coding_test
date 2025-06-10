from sys import stdin
# stdin = open("input.txt","r")
input = stdin.readline

N = int(input())
matrix = []
sorted_matrix = []
for i in range(N):
    matrix.append(tuple(map(int,input().split())))
    sorted_matrix.append((matrix[-1][0],i))

sorted_matrix.sort(key=lambda x: x[0],reverse=True)

dp_start = [x for x in range(N)]
dp_end = [x for x in range(N)]

count = 0
for _, i in sorted_matrix:
    if i == 0:
        continue
    count += matrix[dp_start[i-1]][0] * matrix[i][0] * matrix[dp_end[i]][1]
    dp_start[i] = dp_start[i-1]
    dp_end[i-1] = dp_end[i]

print(count)
            

