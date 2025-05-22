import sys
a,b = map(list,sys.stdin.readline().split())
a.reverse()
b.reverse()
a = "".join(a)
b = "".join(b)

print(a if a>b else b)