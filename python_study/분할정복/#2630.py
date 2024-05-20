import sys
input = sys.stdin.readline  # 시간단축용

n = int(input())    # 색종이 변의 길이
base = [list(map(int,input().split())) for _ in range(n)]   # 색 베이스를 2차원 배열로 세팅
ans_list = []   # 정답을 담을 ans_list 초기화

# 색 구분하는 check함수
def check(x, y, n):
    color = base[x][y]    # 시작점 색을 기준점으로 설정
    # 2중 for문을 통해 전체 색 조사
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != base[i][j]:   # 확인중인 칸의 색이 기준점 색과 다르면
                n2 = n//2   # 길이 절반을 세팅
                # 네개의 구역으로 나누어 재귀호출
                check(x, y, n2)
                check(x, y+n2, n2)
                check(x+n2, y, n2)
                check(x+n2, y+n2, n2)
                return
    # 재귀호출을 할 조건이 아닐때 (해당 구역에 같은 색만 존재할때)
    # 해당 색을 정답 리스트에 입력
    if color == 0:
        ans_list.append(0)
    else:
        ans_list.append(1)

# 함수 실행후 정답 리스트에서 두가지 색 각각 카운트
check(0,0,n)
print(ans_list.count(0))
print(ans_list.count(1))