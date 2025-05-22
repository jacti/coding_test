import sys

N = int(sys.stdin.readline())

def operation(n):
    a, b = 0, 0
    if n < 10:
        b = n
    else:
        a,b = divmod(n,10)
    
    return b*10 + (a+b)%10

n = N
count = 1
n = operation(n)

while n != N:
    n = operation(n)
    count += 1
print(count)