#테스트케이스 개수 t입력
t = int(input())

#crawl 함수 정의
#지렁이가 기어다니며 배추의 해충을 제거하는 과정 정의 
def crawl(x, y):
#좌우, 상하로 기어다니기 위해 이동 조종키 역할을 하는 searchx,y list
    searchx = [1, -1, 0, 0]
    searchy = [0, 0, 1, -1]
#좌우, 상하로 기어다니는 반복문
    for i in range(4):
        cx = x + searchx[i]
        cy = y + searchy[i]
#기어가는 위치가 밭의 크기를 넘지 않도록 함
        if(0 <= cx < n) and (0 <= cy < m):
#기어가는 곳에 배추가 존재하면 해충 제거 완료하고 다시 주변 배추로 이동
            if target[cx][cy] == 1:
                target[cx][cy] = 0
                crawl(cx, cy)

#밭의 크기와 배추의 수를 입력받아 밭을 구성
for p in range(t):
    m, n, k = map(int, input().split())
    target = [[0 for k in range(m)] for p in range(n)]
    cnt = 0
#배추의 위치를 입력받아 밭을 재구성
    for q in range(k):
        a, b = map(int,input().split())
        target[b][a] = 1
#밭을 조사하여 배추가 있으면 crawl 함수를 실행
    for i in range(n):
        for j in range(m):
            if target[i][j] == 1:
                crawl(i, j)
                cnt += 1
#지렁이 수를 출력                  
    print(cnt)