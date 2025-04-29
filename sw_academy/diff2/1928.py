import sys
sys.stdin = open("input.txt", "r")

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcedfghijklmnopqrstuvwxyz0123456789+/'
index = 0
decoding_map = {}
for chr in characters:
    decoding_map[chr] = index
    index+=1

T = int(input())
for test_case in range(1, T + 1):
    txt = input()
    data = [0]
    index = 0
    swift = 18
    for chr in txt:
        data[index] += decoding_map[chr] << swift
        swift -= 6
        if swift < 0:
            swift = 18
            index +=1
            data.append(0)
    result = ""
    for unit in data[:-1]:
        chr1 = (unit & 0xff0000) >> 16
        chr2 = (unit & 0xff00) >> 8
        chr3 = unit & 0xff
        result += str(bytes([chr1,chr2,chr3]),'utf-8')
    print(f"#{test_case} {result}")

