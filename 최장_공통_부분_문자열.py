from sys import stdin
# from collections import deque
# stdin = open("input.txt","r")
input = stdin.readline

str1 =" " + input().rstrip()
str2 = " " + input().rstrip()
index_dict = dict()

for index in range(len(str1)-1,-1,-1):
    txt=str1[index]
    if txt in index_dict:
        index_dict[txt].append(index)
    else:
        index_dict[txt] = [index]
max_count = 0
last_world_index = 0

dp = [(0,0)] * len(str1)
for y in range(1,len(str2)):
    if str2[y] in index_dict:
        for x in index_dict[str2[y]]:
            if dp[x-1][1] == y-1:
                dp[x] = (dp[x-1][0]+1 , y)
            else:
                dp[x] = (1, y)
            if max_count < dp[x][0]:
                max_count = dp[x][0]
                last_world_index = x

result = str1[last_world_index-max_count+1:last_world_index+1]
print(max_count)
print(result)
 
