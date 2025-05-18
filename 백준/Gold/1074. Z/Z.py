import sys

count = 0

def z(size:int, x:int, y:int, c, r):
    global count
    if size ==1:
        if (x,y) == (c,r):
            print(count)
        else:
            count+=1

    elif r < y:
         return

    elif y <= r and r < (y + size):
        if c < x:
              return
        elif c < x+size:
            n = size//2
            z(n, x, y, c,r)
            z(n, x+n, y, c,r)
            z(n, x, y+n, c,r)
            z(n, x+n, y+n, c,r)
        else:
             count += size * size
    else:
        count += size * size
        

N,r,c = map(int,sys.stdin.readline().split())

z(2**N,0,0,c,r)
