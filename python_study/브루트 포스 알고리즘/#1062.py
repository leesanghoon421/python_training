import sys
input = sys.stdin.readline  # 시간단축 코드

N, K = map(int, input().split())    # 단어수를 N으로 배우는 글자수를 K로 입력
words = []  # 단어 종류를 담아둘 리스트 생성
for _ in range(N):  # 단어 수 만큼 반복하여 리스트에 입력
    words.append(input().strip())

alpha = ['a', 'n', 't', 'i', 'c']   # 학습한 알바펫를 담아둘 리스트(a,n,t,i,c)는 필수로 학습
# a,n,t,i,c를 제외한 알파벳 리스트
alpha_list = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
              'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
result = 0

# check function 정의
def check():
    cnt = 0     # cnt를 0으로 초기화
    for w_check in words:   # words리스트 전부 체크
        readable = 1    # 읽을 수 있는 단어임을 확인하는 변수를 1(읽을 수 있음)으로 초기화
        for i in range(4, len(w_check)-4):  # 단어의 문자를 전,후반 4개씩 제외하고 체크
            if w_check[i] not in alpha:     # alpha에 포함되지 않으면
                readable = 0                # 읽을 수 없다고 판단
                break
        if readable == 1:   # 읽을 수 있다면
            cnt += 1        # 카운팅
    return cnt      # check함수의 출력은 cnt

# choose_alpha function 정의
def choose_alpha(n, start):     # 배운 문자수에 따라 알파벳 조합을 연산하는 함수
    global result
    if n == 0:      # n=0 즉 checking이 종료되면   
        result = max(result, check())   # result를 기존의 result와 check함수의 결과인 cnt중 더 큰수로 교체
        return
    # 5개의 default 알파벳을 제외하고 남는 알파벳들의 조합 생성하여 alpha list로 옮겨주는 과정
    for i in range(start, len(alpha_list)):     
        alpha.append(alpha_list[i])
        choose_alpha(n-1, i+1)  # recursion
        alpha.pop()
# 학습한 알파벳이 5개 이하면 어떠한 단어도 읽을 수 없음
if K < 5:
    print(result)
# 무조건 학습할 알파벳 5개를 제외하고 첫번째 알파벳부터 선택하여 전수조사
else:
    choose_alpha(K-5, 0)    
    print(result)