import sys
n = int(input())
txt_list = list(set(txt.rstrip() for txt in sys.stdin.readlines()))

txt_list.sort(key=lambda x : (len(x),x))
for txt in txt_list:
    print(txt)