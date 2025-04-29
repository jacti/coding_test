import sys
sys.stdin = open("input.txt", "r")

N = int(input())
result = []
for i in map(str, range(1,N+1)):
    txt = list(i)
    is_common = True
    new_txt = ""
    for char in txt:
        if char == '3' or char == '6' or char == '9':
            new_txt += '-'
            is_common = False
    if is_common:
        new_txt = i
    result.append(new_txt)
print(" ".join(result))