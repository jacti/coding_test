"""
stack에 탑이 들어올 때 head가 탑보다 클 때까지 pop
append 시점에서 head의 index에서 수신
젤 앞에 0, inf 값의 타워가 있다고 가정
"""

import sys
# sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
towers = []

for i, h in enumerate(map(int,input().split())):
    towers.append((i+1,h))

stack = [(0,float('inf'))]
result =[]
for i, h in towers:
    while h > stack[-1][1]:
        stack.pop()
    result.append(str(stack[-1][0]))
    stack.append((i,h))

print(" ".join(result))