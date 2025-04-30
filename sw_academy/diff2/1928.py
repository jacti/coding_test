import sys
sys.stdin = open("input.txt", "r")

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
index = 0
decoding_map = {}
for char in characters:
    decoding_map[char] = index
    index+=1

T = int(input())
for test_case in range(1, T + 1):
    txt = input()
    buffer = 0
    bits = 0
    decoded_text = ""
    for char in txt:
        buffer = (buffer<<6) + decoding_map[char]
        bits +=6
        if bits == 24:
            while bits>0:
                bits-=8
                decoded_text += chr((buffer >> bits)&0xFF)
            buffer = 0
    print(f"#{test_case} {decoded_text}")

