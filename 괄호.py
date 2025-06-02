import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    stack = 0
    txt = list(input())
    for x in txt:
        if x == '(':
            stack += 1
        elif x == ')':
            stack -=1
            if stack <0:
                print("NO")
                break
    else:
        if stack == 0:
            print("YES")
        else:
            print("NO")