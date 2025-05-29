from sys import stdin
# stdin = open("input.txt","r")
input = stdin.readline

old_txt = list(input().rstrip())
# old_txt = input().rstrip()
bomb_origin = input().rstrip()
bomb = list(bomb_origin)
bomb.reverse()
B = bomb[0]
bomb = bomb[1:]

stack = []
for txt in old_txt:
    if txt != B:
        stack.append(txt)
    else:
        idx = 0
        for b in bomb:
            if stack and idx-1>=-len(stack) and stack[-1 + idx] == b:
                idx -=1
            else:
                stack.append(txt)
                break
        else:
            for _ in range(len(bomb)):
                stack.pop()


result = "".join(stack)

print(result if result else "FRULA")
            
            




# # -- replace를 활용한 방법 : 시간초과 --

# txt_len = len(old_txt)
# old_txt = old_txt.replace(bomb_origin,"")
# if bomb_origin not in old_txt:
#     print(old_txt)
# else:
#     while len(old_txt) != txt_len:
#         txt_len = len(old_txt)
#         old_txt = old_txt.replace(bomb_origin,"")

#     print(old_txt if old_txt else "FRULA")
