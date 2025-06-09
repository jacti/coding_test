n = int(input())

a, b = 0, 1

for _ in range(2,n+1):
    tmp = a
    a = b
    b = a + tmp

print(b)