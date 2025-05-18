index = 0
max_value = 0
for i in range(1,10):
    N = int(input())
    if N > max_value:
        max_value = N
        index = i
print(max_value)
print(index)