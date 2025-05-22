import sys

# 테스트 용 리디렉션 함수
# sys.stdin = open("input.txt","r")
N, S = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
count = 0

# 비트로 사용한 index 저장
# 모든 값을 다 사용했으면 finish
finish = 2**N -1

dp = [False]*(2**N)

def search(num_sum,visited):
    global finish
    global arr
    global N
    global S
    global count
    
    if dp[visited]:
        return
    else:
        dp[visited] = True
    
    if num_sum == S and visited !=0:
        count +=1
    if visited == finish:
        return
    
    not_visited = finish - visited
    
    for i, num in enumerate(arr):
        if not_visited & 0b1 == 1:
            search(num_sum+num, (visited | 1 << i))
        not_visited >>= 1

search(0,0)
print (count)
        



    