import sys
from collections import deque
N, K = map(int,input().split())
q = deque(map(str,range(1,N+1)))

result = []
for _ in range(N):
    for _ in range(K-1):
        q.append(q.popleft())
    result.append(q.popleft())

result = ", ".join(result)

print("<" + result + ">")