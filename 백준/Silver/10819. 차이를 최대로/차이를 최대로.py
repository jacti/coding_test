import sys

def rec(a:int, rest:list[int],sum):
    if len(rest) == 0:
        return sum
    else:
        result = []
        for b in rest:
            new_rest = rest[:]
            new_rest.remove(b)
            result.append(rec(b,new_rest,sum+ abs(b-a)))
        return max(result)
            


N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))

result = []
for i in array:
    rest = array[:]
    rest.remove(i)
    result.append(rec(i,rest,0))
print(max(result))
