import sys

while True:
    array = list(map(int,sys.stdin.readline().split()))
    if array[0] == 0:
        break
    else:
        N = array[0] + 2
        array[0]= 0
        array.append(0)

        stack = [(0,0)]
        max_size = 0

        for i in range(1,N):
            h = array[i]
            if stack[-1][1] < h:
                stack.append((i,h))
                continue
            else:
                i2 = 0
                while stack[-1][1] > h:
                    i2 , h2 = stack.pop()
                    size = (i-i2)*h2
                    if size > max_size:
                        max_size = size
                if stack[-1][1] != h:
                    stack.append((i2,h))

        print(max_size)

