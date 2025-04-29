import sys
sys.stdin = open("input.txt", "r")
class Cards:
    def __init__(self, max_count):
        self.dp = [dict() for _ in range(max_count+1)]

    def find_max(self,attempts,numbers):
        if attempts == 0:
            return numbers
        elif numbers in self.dp[attempts]:
            return self.dp[attempts][numbers]
        else:
            numberList = list(numbers)
            tmp = set()
            for i in range(len(numberList)-1):
                for j in range(i+1,len(numberList)):
                    numberList[i], numberList[j] = numberList[j], numberList[i]
                    newNumber = ''.join(numberList)
                    numberList[i], numberList[j] = numberList[j], numberList[i]
                    tmp.add(self.find_max(attempts-1,newNumber))
            result = max(tmp,key=int)
            self.dp[attempts][numbers] = result
            return result

T = int(input())
for test_case in range(1, T + 1):
    number, count = input().split()
    count = int(count)
    cards = Cards(count)
    print(f"#{test_case} {cards.find_max(count,number)}")