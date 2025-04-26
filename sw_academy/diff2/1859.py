import sys
sys.stdin = open("input.txt","r")
T = int(input())
for test_case in range(1,T+1):
    # 여기서부터 문제 시작
    # 입력은 기간:정수, 가격: 정수
    day = int(input())
    price_list = list(map(int, input().split()))
    # 전략 최대값일땐 무조건 판매
    sorted_list = price_list.sort(reverse=True)
    sum = 0
    result = 0
    index = 0
    for price in price_list:
        if price == sorted_list[index]:
            result += sum
            sum = 0
            index += 1
        else:
            sum += sorted_list[index] - price
    print(f"${test_case}", result)
