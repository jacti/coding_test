N, B = input().rstrip().split()

def c_to_i(n):
    i = ord(n)
    if ord('0')<= i <= ord('9'):
        return i - ord('0')
    if ord('A') <= i <= ord('Z'):
        return i - ord('A') + 10

B = int(B)
num = 0
N = list(N)
N.reverse()

for i, n in enumerate(N):
    num += c_to_i(n) * (B**i)
print(num)

# print(int(N,int(B)))