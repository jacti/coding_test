from sys import stdin
input = stdin.readline

N = int(input())
cards = set(map(int,input().split()))

M = int(input())
numbers = list(map(int,input().split()))

result = []
for num in numbers:
    result.append('1' if num in cards else '0')

print(" ".join(result))

a = {}
a.