# 테스트 위한 함수 실제 실행시 주석처리 할 것
# import sys
# sys.stdin = open("input.txt", "r")

# n 이하의 소수 리스트를 만드는 함수
def setPrimeList(n:int):
    return setPrimeList_while(n)
# for를 사용한 방법 -> 예상대로 동작하지 않음
def setPrimeList_for(n:int):
    primeList = [i for i in range(2,n+1)]
    for num in primeList:
        for otherNum in primeList[1:]:
            if otherNum % num ==0:
                primeList.remove(otherNum)
        
    return primeList

#while을 사용한 방법
def setPrimeList_while(n:int):
    primeList = [i for i in range(2,n+1)]
    i=0
    while(i<len(primeList)):
        j=i+1
        while(j<len(primeList)):
            if primeList[j]%primeList[i] == 0:
                primeList.remove(primeList[j])
            else:
                j+=1
        i+=1
    return primeList


# print(setPrimeList_while(20))
# print(setPrimeList_for(20))

#테스트 케이스 입력
T = int(input())

inputList = []

for _ in range(T):
    inputList.append(int(input()))

#입력 중 가장 큰 값을 n으로 저장
n = max(inputList)
# 같이 쓸 전역 primeList 계산
primeList = setPrimeList(n)

for num in inputList:
    # //TRY 1 : 시간초과
    # a, b, i = 0, num, 0
    # # a, b는 쌍을 이루므로 새 소수를 b 이전까지만 조회하면 됨
    # while primeList[i] < b:
    #     if num - primeList[i] in primeList:
    #         a, b = primeList[i], num - primeList[i]
    #     i += 1
    # print(f"{a} {b}")

    # # //TRY 2 : pass
    # # num/2 부터 조회 양옆으로 조회
    half = num//2

    index = 0
    for i, prime in enumerate(primeList):
        if prime >= half:
            index = i
            break
    
    for prime in primeList[index:]:
        if num - prime in primeList:
            print(f"{num - prime} {prime}")
            break
        
