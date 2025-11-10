from sys import stdin
input = stdin.readline

N= int(input())
count = [[i,0] for i in range(N)]
member = []

for cur in range(N):
    member.append(list(map(int,input().split())))
    for prev in range(cur):
        for grade in range(5):
            if member[cur][grade] == member[prev][grade]:
                count[prev][1] +=1
                count[cur][1] +=1
                break

print(max(count,key=lambda x:x[1])[0] +1)

