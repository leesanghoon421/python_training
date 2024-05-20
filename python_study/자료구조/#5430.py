import sys
from collections import deque

input = sys.stdin.readline
T = int(input())    # 테스트 케이스의 개수 T입력

for i in range(T):
    p = input().strip()     # 함수 입력
    n = int(input())        # 정수 배열의 정수의 수 입력
    err = 0         # 에러 상태인지 확인
    arr = input().strip()   # 정수 배열 입력
    dq = deque(arr[1:-1].split(','))    # []와 , 를 제거하여 deque 자료구조로 dq에 입력
    if n == 0:      # n이 0이면 빈 deque으로 설정
        dq = deque()
    R_cnt = 0           # R연산 횟수 카운터
    for i in range(len(p)):   # 함수의 개수만큼 반복
        if p[i] == 'R':     # R연산 횟수 카운팅
            R_cnt += 1
        elif p[i] == 'D':   # D연산인 경우
            if len(dq) == 0:    # 배열에 남은 수가 없으면
                print('error')  # error 출력
                err = 1         # error 상태로 변경
                break      # 반복문 종료
            else:   # 배열에 남은 수가 있으면
                if R_cnt % 2 == 0:    # R이 짝수번 나오면
                    dq.popleft()      # D연산 진행
                else:       # R이 홀수번 나오면
                    dq.pop()    # 뒤집었다 가정하고 오른쪽수 제거

    if err == 1:    # error 상태이면 반복문 스킵
        continue
    else:   # error 상태가 아닌 경우
        if R_cnt % 2 == 0:  # R이 짝수번 나오면
            print('[' + ",".join(dq) + ']') # 안뒤집고 정답 형태로 출력
        else:   # R이 홀수번 나오면
            dq.reverse()    # 뒤집어서
            print('[' + ",".join(dq) + ']') # 정답 형태로 출력