from sys import stdin
input = stdin.readline
N, K = map(int,input().split())
number = list(input().rstrip())

stack = [number[0]]
for i in number[1:]:
    while stack and K >0 and stack[-1] < i:
        stack.pop()
        K -=1
    stack.append(i)

while K > 0:
    stack.pop()
    K -=1
print("".join(stack))
