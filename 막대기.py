import sys
input = sys.stdin.readline

N = int(input())
stack = []
len_stack = 0
for _ in range(N):
    a = int(input())
    while len_stack>0 and stack[-1] <= a:
        stack.pop()
        len_stack -= 1
    stack.append(a)
    len_stack +=1

print(len_stack)
    