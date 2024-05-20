import sys

input = sys.stdin.readline

n = int(input())    # 몇번의 거래를 진행할지 입력

for _ in range(n):  # 거래 횟수만큼 반복
    days = int(input())     # 몇일동안 거래진행할지 결정
    stock = list(map(int, input().split()))     # 거래일동안 주식가격 리스트
    # 뒤에서부터 서칭을 하여 최대값보다 작으면 바로 이익 실현하는 알고리즘
    stock = list(reversed(stock))       # 역순정렬 리스트로 변경
    max_price = stock[0]       # max_price 초기화
    profit = 0      # 총 이익 0으로 초기화
    # 역순정렬 되었으므로 앞에서부터 max_price를 계속 설정해가며 최대값 이하의 값을 만나면 그 차이를 총이익에 추가
    for price in (stock[1:]):   # 0번 인덱스를 max_price로 설정하였으므로 1번 인덱스부터 조사 진행
        if price > max_price:   # 현재 주가가 max_price보다 크면
            max_price = price   # max_price 재설정
        else:                   # 현재 주가가 max_price보다 크면
            profit += max_price - price     # 그 차이를 총이익에 추가

    print(profit)