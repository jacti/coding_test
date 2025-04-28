import sys
sys.stdin = open("input.txt","r")
T = int(input())
for test_case in range(1,T+1):
    # 여기서부터 문제 시작
    # 입력은 기간:정수, 가격: 정수
    day = int(input())
    price_list = list(map(int, input().split()))
    # 전략 뒤에 부터 조사
    price_list.reverse()
    max = price_list[0]
    sum = 0
    result = 0
    for price in price_list[1:]:
        if price > max:
            max = price
            result += sum
            sum = 0
        else:
            sum += max-price
    result += sum
    print(f"#{test_case}", result)
