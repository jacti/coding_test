import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    numbers, count = input().split()
    count = int(count)
    memory = {numbers}
    temp = [numbers]
    size = len(numbers)

    for _ in range(count):
        temp2 = []
        for number in temp:
            numberList = list(number)
            for i in range(len(numberList)-1):
                for j in range(i+1,len(numberList)):
                    numberList[i], numberList[j] = numberList[j], numberList[i]
                    newNumber = ''.join(numberList)
                    numberList[i], numberList[j] = numberList[j], numberList[i]
                if newNumber in memory:
                    continue
                else:
                    memory.add(newNumber)
                    temp2.append(newNumber)



                