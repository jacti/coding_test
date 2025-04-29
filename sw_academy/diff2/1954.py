import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case}")
    N = int(input())
    result = [[0]*N for _ in range(N)]
    x = 0
    y = 0
    cicle = 0
    direction = 0 # 0 -> right, 1 -> down, 2-> left, 3-> up
    for i in range(1,N*N+1):
        result[y][x] = i
        if direction == 0:
            x+=1
            if x >= N-cicle:
                x-=1
                y+=1
                direction = 1
        elif direction == 1:
            y+=1
            if y>= N-cicle:
                y-=1
                x-=1
                direction = 2
        elif direction == 2:
            x -=1
            if x<0+cicle:
                x+=1
                y-=1
                direction =3
        elif direction == 3:
            y-=1
            if y<1+cicle:
                y+=1
                x+=1
                direction = 0
                cicle +=1
        else:
            raise Exception("wrong direction input")
    
    for row in result:
        print(" ".join(map(str,row)))
