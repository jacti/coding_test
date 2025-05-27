import sys
import bisect

# sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = []

for num in arr:
    idx = bisect.bisect_left(dp, num)
    if idx == len(dp):
        dp.append(num)
    else:
        dp[idx] = num

print(len(dp))