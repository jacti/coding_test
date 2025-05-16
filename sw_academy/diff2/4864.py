import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    keyword = input()
    txt = input()
    size = len(keyword)
    i = 0
    count = 0
    while i != -1:
        i = txt.find(keyword,i)
        if i != -1:
            count += 1
            i += size
    print(f"#{test_case} {count}")