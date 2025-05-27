from sys import stdin

input = stdin.readline

stack = []
txt = list(input().rstrip())
open = {'(','['}
close = {')',']'}

closed = True
for t in txt:
    if not stack:
        if t in close:
            print(0)
            break
        else:
            stack.append(t)
    else:
        if t in open:
            stack.append(t)
        else:
            score =0
            while stack and stack[-1] not in open:
                score += stack.pop()
            if t == ')':
                if not stack or stack[-1] == '[':
                    print(0)
                    break
                elif stack[-1] == '(':
                    stack.pop()
                    stack.append(score*2 if score != 0 else 2)
            elif t == ']':
                if not stack or stack[-1] == '(':
                    print(0)
                    break
                elif stack[-1] == '[':
                    stack.pop()
                    stack.append(score*3 if score != 0 else 3)
else:
    for i in stack:
        if i in open or i in close:
            print(0)
            break
    else:
        print(sum(stack))
        