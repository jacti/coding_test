from sys import stdin
input = stdin.readline

N = int(input())
characters = dict()
for _ in range(N):
    txt = input().rstrip()
    for i,chr in enumerate(txt[::-1]):
        if chr in characters:
            characters[chr] += 10**i
        else:
            characters[chr] = 10**i
            
characters = list(characters.items())
characters.sort(key= lambda x: x[1], reverse= True)

result = 0
for i,(_, count) in enumerate(characters):
    result += (9-i)*count

print(result)