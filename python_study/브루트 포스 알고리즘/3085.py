import sys
input = sys.stdin.readline

n = int(input())
board = [list(input()) for _ in range(n)]   # 게임판을 세팅할 2차원 배열 board정의
max_count = 0       # 결과를 도출할 최대값 카운터 0으로 초기화

def check():        # 같은 색의 사탕이 있나 체크하는 함수
    global max_count    # max_count값을 전역변수로 선언
    for i in range(n):
        cnt = 1            # 기본적을 연속된 사탕의 수는 1로 초기화
        for j in range(n-1):    # 오른쪽 방향 체크
            if board[i][j]==board[i][j+1]:  # 우측 사탕과 색이 일치하면
                cnt += 1                    # cnt값 1증가
                max_count = max(max_count, cnt) # max_count 즉 최대값을 기존의 최대값과 cnt값을 비교하여 더 큰 값으로 갱신
            else:               # 우측 사탕과 색이 일치하지 않으면
                cnt = 1         # 카운터값 1로 다시 초기화
        cnt = 1            # 기본적을 연속된 사탕의 수는 1로 초기화
        for j in range(n-1):    # 아래 방향 체크
            if board[j][i]==board[j+1][i]:  # 하단 사탕과 색이 일치하면
                cnt += 1                    # cnt값 1증가
                max_count = max(max_count, cnt) # max_count 즉 최대값을 기존의 최대값과 cnt값을 비교하여 더 큰 값으로 갱신
            else:               # 우측 사탕과 색이 일치하지 않으면
                cnt = 1         # 카운터값 1로 다시 초기화

for i in range(n):  # (0,0)좌표부터 좌표 전수조사 
    for j in range(n-1):
        # 만약 입력 받은 좌표의 사탕의 색과 우측의 사탕의 색이 다르다면
        if board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j] # 좌우 사탕을 바꿈
            check()     # 최대 수 확인
            board[i][j + 1], board[i][j] = board[i][j], board[i][j + 1] # 사탕을 다시 돌려놓음
        # 만약 입력 받은 좌표의 사탕의 색과 하단의 사탕의 색이 다르다면
        if board[j][i] != board[j + 1][i]:
            board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i] # 상하 사탕을 바꿈
            check()     # 최대 수 확인
            board[j + 1][i], board[j][i] = board[j][i], board[j + 1][i] # 사탕을 다시 돌려놓음

            

print(max_count) #색이 같은 사탕개수 최대값을 출력