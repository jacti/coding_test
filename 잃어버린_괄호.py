from sys import stdin

math = stdin.readline().rstrip()

math = math.split('-')

result = 0


for i, piece in enumerate(math):
    piece = sum(map(int,piece.split('+')))
    result += piece if i ==0 else -piece

print(result)