import sys
input = sys.stdin.readline

N = int(input())
stack= []
for _ in range(N):
    input_txt= input().split()
    op = input_txt[0]
    if op == "push":
        stack.append(input_txt[1])
    elif op == "top":
        try:
            print(stack[-1])
        except:
            print(-1)
    elif op == "size":
        print(len(stack))
    elif op == "empty":
        print(1 if len(stack) == 0 else 0)
    elif op == "pop":
        try:
            print(stack.pop())
        except:
            print(-1)
    else:
        pass