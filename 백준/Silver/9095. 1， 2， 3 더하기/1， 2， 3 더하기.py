import sys
T = int(sys.stdin.readline())

nums = [1,2,3]

def select(rest):
    global nums
    if rest == 0:
        return 1
    else:
        return sum([select(rest-num) for num in nums if rest - num >= 0])
                


for _ in range(T):
    n = int(sys.stdin.readline())
    print(select(n))