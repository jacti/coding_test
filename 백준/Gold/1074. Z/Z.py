import sys

count = 0

def z(size:int, x:int, y:int, c, r):
    global count
    if size ==1:
        if (x,y) == (c,r):
            print(count)
        else:
            count+=1
    elif x+size<c or y+size<r:
            count += size * size
    elif c<x and r<y:
         return
    else:
        n = size//2
        z(n, x, y, c,r)
        z(n, x+n, y, c,r)
        z(n, x, y+n, c,r)
        z(n, x+n, y+n, c,r)

N,r,c = map(int,sys.stdin.readline().split())

z(2**N,0,0,c,r)
